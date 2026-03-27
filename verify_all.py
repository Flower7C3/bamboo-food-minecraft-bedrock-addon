#!/usr/bin/env python3
"""
Comprehensive verification script for Minecraft Bedrock Addon
Verifies project structure, files, and build readiness.

Same helper stack as sibling projects (minecraft_check / console_utils).
Translation + texture checks from minecraft_check target block/catalog-style packs;
this project uses mixed lang keys and item textures, so those steps are omitted
(see warp-points/verify_all.py for the same pattern).
"""
from minecraft_check import MinecraftUtils


def main():
    """Main verification function"""
    MinecraftUtils.verification_summary([
        MinecraftUtils.verify_config,
        MinecraftUtils.verify_manifests,
        MinecraftUtils.verify_project_structure,
        MinecraftUtils.count_project_files,
        MinecraftUtils.verify_blocks,
    ])


if __name__ == "__main__":
    main()
