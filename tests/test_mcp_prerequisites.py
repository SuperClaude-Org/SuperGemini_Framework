import os
import sys
from pathlib import Path

from setup.components.mcp import MCPComponent


def _create_fake_executable(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n", encoding="utf-8")
    try:
        path.chmod(0o755)
    except PermissionError:
        # Windows on some filesystems may not allow chmod; skip silently.
        pass


def test_find_node_in_nvm_versions(monkeypatch, tmp_path):
    fake_home = tmp_path / "home"
    node_dir = fake_home / ".nvm" / "versions" / "node" / "v22.16.0" / "bin"
    node_name = "node.exe" if sys.platform == "win32" else "node"
    node_path = node_dir / node_name
    _create_fake_executable(node_path)

    # Ensure PATH does not already contain the fake executable
    dummy_path = tmp_path / "dummy_path"
    dummy_path.mkdir()
    monkeypatch.setenv("PATH", str(dummy_path))
    monkeypatch.setattr(Path, "home", lambda: fake_home)

    component = MCPComponent(install_dir=tmp_path)
    found = component._find_executable_with_fallbacks("node")

    assert found == str(node_path)


def test_find_uv_in_cargo_bin(monkeypatch, tmp_path):
    fake_home = tmp_path / "home"
    uv_dir = fake_home / ".cargo" / "bin"
    uv_name = "uv.exe" if sys.platform == "win32" else "uv"
    uv_path = uv_dir / uv_name
    _create_fake_executable(uv_path)

    dummy_path = tmp_path / "dummy_path"
    dummy_path.mkdir(exist_ok=True)
    monkeypatch.setenv("PATH", str(dummy_path))
    monkeypatch.setattr(Path, "home", lambda: fake_home)

    component = MCPComponent(install_dir=tmp_path)
    found = component._find_executable_with_fallbacks("uv")

    assert found == str(uv_path)


def test_get_expanded_env_adds_version_manager_paths(monkeypatch, tmp_path):
    fake_home = tmp_path / "home"
    cargo_dir = fake_home / ".cargo" / "bin"
    nvm_bin = fake_home / ".nvm" / "versions" / "node" / "v21.0.0" / "bin"

    cargo_dir.mkdir(parents=True, exist_ok=True)
    nvm_bin.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(Path, "home", lambda: fake_home)

    component = MCPComponent(install_dir=tmp_path)
    env = component._get_expanded_env()
    path_entries = env["PATH"].split(os.pathsep)

    assert str(cargo_dir) in path_entries
    assert str(nvm_bin) in path_entries
