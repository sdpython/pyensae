"""
@file
@brief Helper to download jars from MAVEN (for Pig, Hadoop)
"""
import os
import urllib
import urllib.request


def download_jar_from_maven(group, lib, version, location, overwrite=False):
    """
    download a jar file from maven

    @param  group       group
    @param  lib         lib name
    @param  version     version
    @param  location    location
    @return             filename
    """
    group = group.replace(".", "/")
    url = "http://central.maven.org/maven2/{2}/{0}/{1}/{0}-{1}.jar".format(
        lib,
        version,
        group)
    final = os.path.join(location, "{0}-{1}.jar".format(lib, version))

    if not os.path.exists(location):
        raise FileNotFoundError(location)

    if os.path.exists(final) and not overwrite:
        return final
    else:
        try:
            u = urllib.request.urlopen(url)
            alls = u.read()
            u.close()
        except Exception as e:
            raise FileNotFoundError(url) from e

        with open(final, "wb") as f:
            f.write(alls)

        return final
