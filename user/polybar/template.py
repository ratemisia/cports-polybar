pkgname = "polybar"
pkgver = "3.7.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cairo-devel",
    "cmake",
    "libuv-devel",
    "ninja",
    "pkgconf",
    "python",
    "python-packaging",
    "python-sphinx",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-wm-devel",
]
depends = [
    "cairo",
    "libuv",
    "libxcb",
    "xcb-util",
    "xcb-util-image",
    "xcb-util-wm",
    "xcbproto",
]
pkgdesc = "Fast and easy-to-use status bar"
license = "MIT"
url = "https://github.com/polybar/polybar"
source = f"{url}/releases/download/{pkgver}/polybar-{pkgver}.tar.gz"
sha256 = "e2feacbd02e7c94baed7f50b13bcbf307d95df0325c3ecae443289ba5b56af29"


def post_install(self):
    self.install_license("LICENSE")
