
.. blogpost::
    :title: Yahoo finance needs cookie (2)
    :keywords: module, pyenbc
    :date: 2017-12-27
    :categories: module

    I wrote about :epkg:`Yahoo Finance <https://finance.yahoo.com/>`_
    was difficult to automate:
    :ref:`Yahoo finance needs cookie <blog-yahoo-finance-201711>`.
    A module handles was implemented to go around that obstacle:
    `yahoo-historical <https://github.com/AndrewRPorter/yahoo-historical>`_.
    Just added it to :class:`StockPrices <pyensae.finance.astock.StockPrices>`
    when specifying ``url='yahoo_new'``.
