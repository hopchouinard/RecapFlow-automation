"""The tested development request guard, scoped to one approved manual identity."""

from community_brain.jobs.acquisition import Fathom


class SelectedFathom(Fathom):
    def __init__(self, key, recording, started_at, transport=None):
        super().__init__(key, transport)
        if self.call_id(recording) is None:
            raise ValueError("numeric recording ID required")
        self.recording, self.started_at = recording, started_at
        self.lookup_count = self.transcript_count = 0
        self.client.event_hooks["request"] = [self.guard]

    def guard(self, request):
        if (
            request.method != "GET"
            or request.url.scheme != "https"
            or request.url.host != "api.fathom.ai"
        ):
            raise ValueError("only selected Fathom reads permitted")
        if request.url.path == "/external/v1/meetings":
            self.lookup_count += 1
            if self.lookup_count > 5:
                raise ValueError("metadata page ceiling reached")
            request.url = request.url.copy_merge_params(
                {
                    "include_transcript": "false",
                    "include_summary": "false",
                    "include_action_items": "false",
                    "include_highlights": "false",
                    "include_crm_matches": "false",
                }
            )
        elif request.url.path == f"/external/v1/recordings/{getattr(self, 'resolved_recording', None)}/transcript":
            self.transcript_count += 1
            if self.transcript_count > 1:
                raise ValueError("transcript already requested")
        else:
            raise ValueError("unselected Fathom operation")

    def fetch(self, identity):
        if (
            identity["meeting_id"] != self.recording
            or identity["started_at"] != self.started_at
        ):
            raise ValueError("selected recording/time mismatch")
        return super().fetch(identity)
