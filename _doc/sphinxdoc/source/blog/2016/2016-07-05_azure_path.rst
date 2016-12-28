
.. blogpost::
    :title: Convention for path in class MagicAzure
    :keywords: Azure, magic command
    :date: 2016-07-05
    :categories: Azure
    :lid: l-magic-path-container

    For all the magic commands associated to Azure
    (class :class:`MagicAzure <pyensae.remote.magic_azure.MagicAzure>`),
    the path ``/part1/part2``
    is converted into ``container/part1/part2``. For path ``part1/part2``,
    ``path1`` is the container.
