from toolchain import CythonRecipe


class IosRecipe(CythonRecipe):
    version = "master"
    url = "src"
    library = "libios.a"
    depends = ["python"]
    pbx_frameworks = ["MessageUI", "CoreMotion", "UIKit"]

    def install(self):
        self.install_python_package(
            name=self.so_filename("ios"), is_dir=False)


recipe = IosRecipe()
