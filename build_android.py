import os
import shutil
import common as cmn

# Toolchain path
NDK_PATH = "/opt/android-sdk-linux/android-ndk-r23"
TOOLCHAIN = os.path.join(NDK_PATH, "build/cmake/android.toolchain.cmake")
ANDROID_PLATFORM = "28"

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "android")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_libjpeg("x86_64", "Debug")
  Build_libjpeg("x86_64", "Release")
  Build_libjpeg("arm64-v8a", "Debug")
  Build_libjpeg("arm64-v8a", "Release")

#------------------------------------------------------------
# libjpeg-turboビルド
#    host       "x86_64" or "arm64-v8a"
#    build_type "Debug" or "Release"
def Build_libjpeg(host, build_type):
  cmn.Log("Build libjpeg-turbo host=" + host + " build_type=" + build_type)
  INSTALL_PREFIX = os.path.join(INSTALL_PREFIX_OS, host, build_type)
  os.chdir(cmn.LIBJPEG_DIR)
  shutil.rmtree("build", ignore_errors=True)
  os.makedirs("build", exist_ok=True)
  os.chdir("build")
  # cmake generator
  cmd = ["cmake"]
  cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN]
  cmd += ["-DANDROID_ABI=" + host]
  cmd += ["-DANDROID_PLATFORM=" + ANDROID_PLATFORM]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += [".."]
  cmn.Do(cmd)
  # cmake build
  cmd = ["cmake --build ."]
  cmd += ["--config " + build_type]
  cmn.Do(cmd)
  # cmake install
  cmd = ["cmake --install ."]
  cmd += ["--config " + build_type]
  cmn.Do(cmd)


if __name__ == '__main__':
    main()
