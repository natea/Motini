Motini
======

Motini is a tool to easily theme a website using a point-n-click interface. By identifying elements from your content source and identifying where in your theme you want those elements to go, you can create rules that will move the dynamic content from your CMS or dynamic web application.

How does it work
================

Motini works by leveraging the Deliverance middleware proxy, which reads a rules file that tells Deliverance which elements in your content source should be mapped to which placeholder elements in your static theme. It uses common CSS selectors to identify these elements, but it also works with XPath expressions.

Motini provides a jQuery-based UI to select these elements and write out the resulting rules file as XML. This rules file can then be used in a production environment with the Deliverance proxy using these rules to govern the HTML transformations. The Deliverance proxy sits in between Apache (or whatever HTTP server you use) and your CMS to transform the HTML before it's returned to the browser.

Getting started with Motini
===========================

Once you've installed Motini, you start up the proxy with this command::

    $ python motini_simple.py
    serving on 0.0.0.0:8000 view at http://127.0.0.1:8000
    
Then you can go to http://127.0.0.1:8000/start/ in your browser to see the Motini interface.

Motini loads two panes in the browser: a source pane on the left and a destination pane on the right. 
For the source pane, you can use either a remote source or a local source.

Remote source
-------------

In the source pane, you supply a URL of a content source that you want to theme. 
For example, if you enter http://drupal.org, then it will load the Drupal site in the left source pane.

Local source
------------

Or you can reference a site running on localhost. For example, if you have a Plone site running on localhost port 8080 with a site ID of Plone, you would enter this into the URL box::

    http://localhost:8080/Plone

Destination
-----------

This is the final theme that you want to use for your site. The destination pane is loaded with the theme in the folder motini/content/theme. If you want to use a different theme than the one supplied, you can put it in the content directory and give it the name "theme". It should contain an index.html file.

Future enhancements
===================

Configurable theme
------------------

Currently, there is a single theme that is used when you start up Motini.
Eventually, the themes will be configurable and you can select which theme you want to use from a dropdown menu. 
If you don't like any of the supplied themes, there will be a facility to upload a zip file with the theme you want to use.
You will also be able to reference a remote URL of the theme you wish to use, so that no uploading is necessary - just use a live site as your theme.

Per section theming
-------------------

Currently, you can only use a single theme file (index.html), which must be applied to all pages on your site. Deliverance supports multiple page classes, so you can use a different theme file for different sections on your site. For example, you can use frontpage.html to have a different theme file for the front page than the rest of the site::

    <match path="exact:/" class="frontpage" />
    
    <rule class="frontpage">
        <theme href="/theme/frontpage.html" />           
    </rule>
    
    <rule class="default">
        <theme href="/theme/index.html" />
    </rule>
    
What this says is that if a request comes in for / then it should apply the page class "frontpage" which defines a different theme file (frontpage.html), than the standard pages which should use index.html.

We'll need to build an interface in Motini to select from various .html files in the /theme folder and specify a match path expression so that Deliverance knows what paths correspond to which theme files.

Resources
=========

Deliverance: http://deliveranceproject.org
Screencast: http://www.youtube.com/watch?v=MIYiDIK5z6c
