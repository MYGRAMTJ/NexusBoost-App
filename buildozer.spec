[app]
title = NexusBoost
package.name = nexusboost
package.domain = org.nexus
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
source.exclude_patterns = tests, bin, venv, .git, lib/test/*, **/test*, **/tests*, *.pyc, __pycache__/*, .buildozer/*
requirements = python3,kivy==2.3.0

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 1
