from setuptools import setup

setup(name="prewikka-IpMap",
      version="1.0.0",
      author="David Casier",
      author_email="john.doe@acme.com",
      url="https://prelude-siem.org",
      packages=["ipmap"],
      install_requires=["prewikka"],
      entry_points={
          "prewikka.views": [
              "IpMap = ipmap:IpMap",
          ],
      },
      package_data={
        "ipmap":["htdocs/css/*.css","templates/*.py", "htdocs/txt/*.txt", "htdocs/img/*.png", "htdocs/txt/*.dat", "htdocs/map_js/*.js", "htdocs/map_js/*.css", "htdocs/map_js/tests/assets/*.js", "htdocs/map_js/lib/*.js", "htdocs/map_js/src/*.js","htdocs/js/*.js"],
        },
)
