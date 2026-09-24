"""Exact human identities and per-app permissions authorized by request018."""
HUMANS = {6: "36812476-ed34-4073-a1a5-ae3ad53b1781", 4: "dfae6a7f-e5a5-4575-9796-8187cbdd45b1"}
APPS = {
 "community-brain": {"provider": 8, "group": "69a3fcd8-fc2d-4ad2-b565-41f15c40701a", "group_name": "community-brain-operators", "mapping": "962deddf-1792-4e27-9e01-b0c9249dae2b", "permissions": ["jobs:read", "artifacts:read", "retrieval:read", "jobs:submit", "sources:upload"]},
 "community-brain-dev": {"provider": 7, "group": "291e026d-b5d5-4871-beb2-af01750233b3", "group_name": "community-brain-dev-operators", "mapping": "a3b5a36d-daa8-41d2-852a-83a6dfc6534f", "permissions": ["jobs:read", "jobs:submit", "jobs:retry", "jobs:rerun", "jobs:reconcile", "sources:upload", "artifacts:read", "retrieval:read"]},
}
def predicate(slug):
 a=APPS[slug]
 return ("request.user.is_active and "
         + repr(HUMANS) + ".get(request.user.pk) == str(request.user.uuid) and "
         + "request.user.groups.filter(pk=" + repr(a['group']) + ").exists()")
def mapping_expression(slug):
 return "if not (" + predicate(slug) + "):\n    return {}\nreturn " + repr({'cb_scope':slug,'cb_permissions':APPS[slug]['permissions']})
def policy_expression(slug):
 return "return " + predicate(slug)
