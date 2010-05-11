<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
            <title>Motini</title>

      <script type="text/javascript" src="/js/jquery-1.3.2.min.js"></script>
      <script type="text/javascript" src="/js/jquery-ui-1.7.1.custom.min.js"></script>
      <script type="text/javascript" src="/js/jquery.layout.min.js"></script>
      <script type="text/javascript" src="/js/banjo.js"></script>
      <link rel="stylesheet" href="/css/banjo.css" type="text/css" media="screen" title="no title" charset="utf-8">
      <link rel="stylesheet" href="/css/smoothness/jquery-ui-1.7.1.custom.css" type="text/css" media="screen" title="no title" charset="utf-8">

    </head>

    <body>

      <div id="info">
          
        <div id="status_box">
          MOTINI
        </div>
        
        <div id="controls_box">
              <h1>Type in the URL of a site you want to theme</h1>
              <form id="url_form" method="GET" action="" >
                <label>URL:</label> <input type="text" id="u" name="u" value="${url}" />
                <input type="submit" value="Theme it!" />
              </form>
        </div>

        <div id="actions_box">
              <a href="/rules.xml">Show current rules</a><br/>
              <a id="clear_rules" href="#">Clear rules</a><br/>
              <img id="loading" src="/images/ajax-loader.gif"/>

        </div>
      </div>
      
% if url:
        <iframe id="delivsource" name="delivsource" src="/motini/clip/${url}"></iframe>
        <iframe id="delivtarget" name="delivtarget" src="/motini/theme/${url}"></iframe>
% else:
        <div id="delivsource">
            <div style="width:500px; margin:50px;">
<h1>
    What is Motini?
</h1>
<p>
    Motini is a tool to easily theme a website using a point-n-click interface. By identifying elements from your content source and identifying where in your theme you want those elements to go, you can create rules that will move the dynamic content from your CMS or dynamic web application.
</p>
<h2>
    How does it work
</h2>
<p>
    Motini works by leveraging <a href="http://deliveranceproject.org">Deliverance</a>, a middleware proxy which reads a rules file that tells Deliverance which elements in your content source should be mapped to which placeholder elements in your static theme. It uses common CSS selectors to identify these elements, but it also works with XPath expressions.
</p>
<p>
    Motini provides a point-n-click to select these elements and write out the resulting rules file as XML. This rules file can then be used in a production environment with the Deliverance proxy using these rules to govern the HTML transformations. The Deliverance proxy sits in between Apache (or whatever HTTP server you use) and your CMS to transform the HTML before it's returned to the browser.
</p>
<h2>
    Getting started
</h2>
<p>
    Motini loads two panes in the browser: a source pane on the left and a destination pane on the right.
</p>
<p>
    In the source pane, you supply a URL of a content source that you want to theme. For example, if you enter http://drupal.org, then it will load the Drupal site in the left source pane.
</p>
<p>
    In the destination pane is the theme that you want to use for your site. Currently, there is only one theme available, but in the future we plan to make many themes available, and even provide the option to supply your own theme.
</p>
<h2>
    How can I learn more?
</h2>
<p>Sign up to be on the announcement list to be notified when Motini is ready for public use. See the signup form on the right.</p>
<p>
    If you are a developer and want to get involved, you can check out the <a href="http://github.com/natea/Motini">code</a> on Github and join the <a href="http://groups.google.com/group/motini-dev/">Motini developers list.</a> <a name="#signup"></a>
</p>
</div>
</div>
        <div id="delivtarget">
        <h2>Short video tutorial</h2>
<object width="560" height="340"><param name="movie" value="http://www.youtube.com/v/MIYiDIK5z6c&hl=en_US&fs=1&rel=0&color1=0x006699&color2=0x54abd6"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/MIYiDIK5z6c&hl=en_US&fs=1&rel=0&color1=0x006699&color2=0x54abd6" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="560" height="340"></embed></object>

        <h2>Signup for more info</h2>
        <p>
            <iframe src="http://spreadsheets.google.com/embeddedform?key=t-kqsAwyZhErhkOQ0jlXEHQ" width="400" height="691" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
        </p>
        
%endif
        </div>

</body>
</html>