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
          <img src='/images/motini-logo-200.jpg' alt="Motini" id="logo" />
        </div>
        <!-- <div id="rules_box"> -->
    <div id="controls_box">
          <h1>Mix your own Motini!</h1>
          <form id="url_form" method="GET" action="" >
            <label>URL:</label> <input type="text" id="u" name="u" value="${url}" />
            <input type="submit" value="Mix" />
          </form>
    </div>

    <div id="actions_box">
          <h1><a href="/rules.xml">Show the current rules</a></h1>
          <div id="rules"></div>
            <a id="clear_rules" href="#">Dump out this Motinin and start over.</a><br/>
          <img id="loading" src="/images/ajax-loader.gif"/>
            <h4>To save your Motini you have to <strong>create an account</strong>.</h4>

    </div>
      </div>
      
% if url:
        <iframe id="delivsource" name="delivsource" src="/motini/clip/${url}"></iframe>
        <iframe id="delivtarget" name="delivtarget" src="/motini/theme/${url}"></iframe>
% else:
        <div id="delivsource">
        <h2>Type in a URL to mix into a Motini!</h2>
%endif
    </div>

</body>
</html>