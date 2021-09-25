import os
import shutil
import common as cmn

# Toolchain path
TOOLCHAIN_x86_64 = os.path.join(cmn.TOP_DIR, "cmake", "x86_64.gcc.toolchain.cmake")
TOOLCHAIN_arm64 = os.path.join(cmn.TOP_DIR, "cmake", "aarch64.gcc.toolchain.cmake")

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "linux")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_libjpeg("x86_64", "Debug")
  Build_libjpeg("x86_64", "Release")
  Build_libjpeg("arm64", "Debug")
  Build_libjpeg("arm64", "Release")

#------------------------------------------------------------
# libjpeg-turboビルド
#    host       "x86_64" or "arm64"
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
  if host == "x86_64":
    cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN_x86_64]
  else:
    cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN_arm64]
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
