<?xml version="1.0"?>
    <ruleset>
    <match path="/motini/theme" class="swap"/>
    <rule class="swap" suppress-standard="1">
    <!--  <theme href="/theme/iphone.html"/>-->
    	<theme href="/theme/index.html"/>
% if rules:
% for rule in rules:
    <${rule.action} content="${rule.content}" theme="${rule.theme}" />
% endfor
%endif
</rule>
</ruleset>