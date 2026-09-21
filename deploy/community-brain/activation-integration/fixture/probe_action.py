"""Synthetic admin-only action exercising the real application's filter cache."""
import hashlib
from open_webui.models.functions import Functions
from open_webui.utils.filter import process_filter_functions, get_function_module


class Action:
    async def action(self, body, __request__, __user__):
        assert __user__.get('role') == 'admin'
        fid = 'community_brain_filter'
        function = Functions.get_function_by_id(fid)
        assert function.is_active and function.is_global
        source_hash = hashlib.sha256(function.content.encode()).hexdigest()
        assert source_hash == '12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16'
        result, _ = await process_filter_functions(
            __request__, [function], 'inlet',
            {'messages': [{'role': 'user', 'content': 'Synthetic migration question'}]},
            {'__user__': __user__})
        module = get_function_module(__request__, fid)
        status, chunks = module._retrieve_chunks('Synthetic migration question')
        context = result['messages'][0]
        return {'live_app_process': True, 'source_sha256': source_hash,
                'effective_url': module.valves.retrieval_url,
                'effective_token_sha256': hashlib.sha256(module.valves.api_key.encode()).hexdigest(),
                'retrieval_status': status, 'source_count': len(chunks),
                'context_emitted': '<transcript_data>' in context.get('content', ''),
                'unavailable_context': 'RETRIEVAL SYSTEM ERROR' in context.get('content', '')}
