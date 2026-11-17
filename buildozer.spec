[app]
title = Nmap App
package.name = nmapapp
package.domain = org.nmapapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
