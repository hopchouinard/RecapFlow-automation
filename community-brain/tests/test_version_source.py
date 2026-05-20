"""Version source must be canonical: pyproject.toml → importlib.metadata."""
from importlib.metadata import version

from community_brain.query.retrieval_server import app


def test_fastapi_app_version_matches_package_metadata():
    """FastAPI app.version must read from package metadata, not a hardcoded string."""
    expected = version("community-brain")
    assert app.version == expected, (
        f"app.version={app.version!r} but package metadata says {expected!r}. "
        f"Read from importlib.metadata.version('community-brain') instead of "
        f"hardcoding."
    )


def test_app_version_is_pep440_compatible():
    """app.version must be a non-empty PEP 440 compatible string.

    Guards against the sentinel-fallback path producing an obviously broken value.
    """
    assert app.version
    assert isinstance(app.version, str)
    # PEP 440: must contain at least a digit. The "0.0.0+uninstalled" sentinel passes.
    assert any(c.isdigit() for c in app.version)
