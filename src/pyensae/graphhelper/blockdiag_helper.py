# -*- coding: utf-8 -*-
"""
@file
@brief Various functions about :epkg:`blockdiag`.

.. versionadded:: 1.1
"""
import os
import io
import glob


def _create_fontmap(fontmap, font):
    """
    Inspired from :epkg:`blockdiag` source file (*_bootstrap.py*).
    """
    from blockdiag.utils.fontmap import FontMap
    fontmap = FontMap(fontmap)
    if fontmap.find().path is None or font:
        fontpath = _detectfont(font)
        fontmap.set_default_font(fontpath)
    return fontmap


def _build_diagram(module, builder, drawer, tree, type, code,
                   fontmap=None, antialias=True, nodoctype=False,
                   transparency=False, size=None):
    """
    Inspired from :epkg:`blockdiag` source file (*_bootstrap.py*).
    """
    ScreenNodeBuilder = builder.ScreenNodeBuilder
    diagram = ScreenNodeBuilder.build(tree, None)

    DiagramDraw = drawer.DiagramDraw
    drawer = DiagramDraw(type, diagram, fontmap=fontmap,
                         code=code, antialias=antialias,
                         nodoctype=nodoctype, transparency=transparency)
    drawer.draw()

    if size:
        return drawer.save(size=size)
    else:
        return drawer.save()


def _detectfont(font):
    fontdirs = [
        '/usr/share/fonts',
        '/Library/Fonts',
        '/System/Library/Fonts',
        'c:/windows/fonts',
        '/usr/local/share/font-*',
    ]
    fontfiles = [
        'ipagp.ttf',
        'ipagp.otf',
        'VL-PGothic-Regular.ttf',
        'Hiragino Sans GB W3.otf',
        'AppleGothic.ttf',
        'msgothic.ttf',
        'msgoth04.ttf',
        'msgothic.ttc',
    ]

    fontpath = None
    if font:
        from blockdiag.utils.fontmap import parse_fontpath
        for path in font:
            _path, _ = parse_fontpath(path)
            if os.path.isfile(_path):
                fontpath = path
                break
        else:
            msg = 'fontfile is not found: %s' % font
            raise RuntimeError(msg)

    if fontpath is None:
        globber = (glob.glob(d) for d in fontdirs)
        for fontdir in sum(globber, []):
            for root, _, files in os.walk(fontdir):
                for font_ in fontfiles:
                    if font_ in files:
                        fontpath = os.path.join(root, font_)
                        break

    return fontpath


def draw_diagram(graph, module="blockdiag", format="pillow", **options):
    """
    Draws a graph based on module :epkg:`blockdiag`.

    @param      graph       graph definition,
                            see `syntax <http://blockdiag.com/en/blockdiag/examples.html>`_
    @param      module      ``'blockdiag'`` (only available value)
    @param      format      can be a filename or a module name (``'pillow'``)
    @param      options     additional options for :epkg:`blockdiag`
    @return                 graph

    ::

        blockdiag {
            A -> B -> C -> D;
            A -> E -> F -> G;
        }

    See notebook :ref:`drawdiagramrst`.
    """
    if module == "blockdiag":
        import blockdiag  # pylint: disable=C0415
        module = blockdiag
        import blockdiag.parser  # pylint: disable=C0415
        parser = blockdiag.parser
        import blockdiag.builder  # pylint: disable=C0415
        builder = blockdiag.builder
        import blockdiag.drawer  # pylint: disable=C0415
        drawer = blockdiag.drawer
    else:
        raise ValueError(
            "Unexected value for 'blockdiag': '{0}'".format(module))

    if format in ("pillow", "png"):
        ftype = "png"
    elif format == "svg":
        ftype = "svg"
    else:
        raise ValueError("format should in ['pillow', 'svg']")

    fontmap = _create_fontmap(fontmap=options.get('fontmap', None),
                              font=options.get('font', None))
    tree = parser.parse_string(graph)
    res = _build_diagram(module=module, builder=builder, drawer=drawer,
                         tree=tree, code=graph, fontmap=fontmap, type=ftype,
                         antialias=options.get('antialias', True),
                         nodoctype=options.get('nodoctype', False),
                         transparency=options.get('transparency', False),
                         size=options.get('size', None))
    if format == "pillow":
        from PIL import Image
        image = Image.open(io.BytesIO(res))
        return image
    else:
        return res
