function RuleSet() {
    this.rules = [];
}

RuleSet.prototype.addRule = function(rule) {
    this.rules.push(rule);
}

RuleSet.prototype.removeRule = function() {
    return this.rules.pop();
}

RuleSet.prototype.clearRules = function() {
    this.rules = [];
}

RuleSet.prototype.serialize = function(separator) {
    if (!separator) {
        separator = "";
    }
    return this.rules.join(separator);
}

RuleSet.prototype.toXMLString = function(separator) {
    if (!separator) {
        separator = "";
    }
    return jQuery.map(this.rules, function(n,i) {
        return n.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }).join(separator);
}

function currentSelection() {}
function selectorHL(src,top,left,height,width,stroke,color,my_id) {
    var src = src;

    this.createEdge = function(top,left,height,width) {
        side = $('<div><!-- --></div>')
        $(side).css({
            'position':'absolute',
            'top':top,
            'left':left,
            'height':height+'px',
            'width':width+'px',
            'background':color,
            'z-index':100});
        side.addClass(my_id+'_selector_side');    
        return side;
    }

    this.clear = function() {
        $(src).find('.'+my_id+'_selector_side').remove();
    }
    
    this.fade = function() {
        $(src).find('.'+my_id+'_selector_side').fadeOut("slow",this.clear);
    }

    this.left = this.createEdge(top,left,height,stroke);
    this.right = this.createEdge(top,left + width - stroke,height,stroke);
    this.top = this.createEdge(top,left, stroke, width) ; //,height-stroke,stroke);
    this.bottom = this.createEdge(top+height - stroke, left, stroke, width);
    
    $(src).append(this.left);
    $(src).append(this.right);
    $(src).append(this.top);
    $(src).append(this.bottom);

    return this;
}

function DeliveranceRule() {
    this.contentRule = "";
    this.themeRule = "";
}
DeliveranceRule.prototype.toDeliveranceXML = function() {
    return '<replace content="children:' + this.contentRule + '" theme="children:' + this.themeRule + '" />';
};

function getCSSSelector(obj) {
    var selector = "";
    var id = "";

    while (!id && obj.parents) {
        id = obj.attr('id');
        if (id) {
            return jQuery.trim(obj[0].tagName.toLowerCase() + "#" + id + " " + selector);
        } else {
            var tag = obj[0].tagName.toLowerCase();
            if (obj.attr('class')) {
                tag = tag + "." + obj.attr('class').replace(' ', '.');
            }
            selector = tag + " " + selector;
            if (tag === 'html') {
                return jQuery.trim(selector);
            }
            obj = obj.parent();
            if (!obj) {
                return jQuery.trim(selector);
            }
        }
    }
}

//
// Global vars. needs refactor.
//

var elementCounter = 1;
var elementStore = [];
var currentDeliveranceRule = new DeliveranceRule();
var myLayout; // a var is required because this page utilizes: myLayout.allowOverflow() method
var rules = new RuleSet(); // array of rules
var cs = new currentSelection();
var ss;
var ts;
var template = '<ruleset>\
  <server-settings>\
    <server>0.0.0.0:8000</server>\
    <execute-pyref>true</execute-pyref>\
    <dev-allow>127.0.0.1</dev-allow>\
	<dev-user username="guest" password="guest" />\
  </server-settings>\
  <proxy path="/_theme" editable="1">\
    <dest href="{here}/../theme" />\
  </proxy>\
  <proxy path="/start">\
    <dest href="{here}/../banjo" />\
  </proxy>\
  <proxy path="/_site/jquery.com" class="frontpage">\
    <response rewrite-links="1"/>\
    <dest href="http://localhost:8000/iframe/jquery.com" />\
  </proxy>\
  <proxy path="/iframe/jquery.com">\
    <response rewrite-links="1"/>\
    <dest href="http://jquery.com" />\
  </proxy>\
  <match path="exact:/" class="splashpage" />\
  <rule class="frontpage" suppress-standard="1">\
    <theme href="/_theme/index.html" />\
    ####XML####\
  </rule>\
  <rule class="splashpage" suppress-standard="1">\
	<theme href="/_theme/splashpage.html" />\
  </rule>\
</ruleset>';
//////
////// ONLOAD STUFF
//////

$(document).ready(function() {

	myLayout = $('body').layout({
        center__paneSelector:   "#delivtarget",
        west__paneSelector:     "#delivsource",
        // west__size:             Math.floor(window.innerWidth / 4),
        // east__paneSelector:    "#preview",
        // center__size:           Math.floor(window.innerWidth / 8),
        west__size:             Math.floor(window.innerWidth / 2),
        // west__size:             Math.floor(window.innerWidth / 2),
		north__paneSelector:    "#info",
        north__size:            "120"
	});

    // $('#edit_rules').click(
function AddRule() {
        // e.stopPropagation();
        // post to /.deliverance/edit_rules
        $('#actions').hide();
        $('#loading').show();
        //"/start/.deliverance/edit_rules",
        //{ content: template.replace(/####XML####/, rules.serialize()) }
        jQuery.post("/start", rules.rules[0],
            function(data, textStatus) {
                    // function() {
                            rules.clearRules();
                    if (textStatus === "success") {
                        window.frames[1].location.reload();
                        // $('#rules').html(rules.toXMLString("<br/>"));
                        $("#url").show();
                        $('#actions').show();
                        $('#loading').hide();
                    } else {
                        alert('Oh no! An error occurred. Please try again later.')
                        $('#actions').show();
                        $('#loading').hide();
                    }
                // }
            }
        );
    };

    $('#undo_rule').click(function(e) {
        e.stopPropagation();
        rules.removeRule();
        // $('#rules').html(rules.toXMLString("<br/>"))
    });
    
    $('#clear_rules').click(function(e) {
        e.stopPropagation();
        $('#actions').hide();
        $('#loading').show();
        rules.clearRules();
        // $('#rules').html(rules.toXMLString("<br/>"))
        jQuery.post("/start", {'command':'clear'},
            function(data, textStatus) {
                // window.setTimeout(function() {
                            rules.clearRules();
                    if (textStatus === "success") {
                        window.frames[1].location.reload();
                        // $('#rules').html(rules.toXMLString("<br/>"));
                        $("#url").show();
                        $('#actions').show();
                        $('#loading').hide();
                    } else {
                        alert('Oh no! An error occurred. Please try again later.')
                        $('#actions').show();
                        $('#loading').hide();
                    }
                // }, 3000);
            }
        );


    });
    
    
        // $('#edit_rules').click(
    function addRule() {
            // e.stopPropagation();
            // post to /.deliverance/edit_rules
            $('#actions').hide();
            $('#loading').show();
            //"/start/.deliverance/edit_rules",
            //{ content: template.replace(/####XML####/, rules.serialize()) }
            jQuery.post("/start", rules.rules[0],
                function(data, textStatus) {
                    // window.setTimeout(function() {
                                rules.clearRules();
                        if (textStatus === "success") {
                            window.frames[1].location.reload();
                            // $('#rules').html(rules.toXMLString("<br/>"));
                            $("#url").show();
                            $('#actions').show();
                            $('#loading').hide();
                        } else {
                            alert('Oh no! An error occurred. Please try again later.')
                            $('#actions').show();
                            $('#loading').hide();
                        }
                    // }, 3000);
                }
            );
        };
    
    

    $('#delivsource').load(function() {
        var src_body = $(this).contents().find("body");
        var current;

        $(src_body).click(
            function(e) {
                e.stopImmediatePropagation();
                // get some sort of css selector based around the html id.
                var selector = getCSSSelector($(cs.current_highlight));
                $('#status').html($('#status').html() + "Source: " + selector +"<br/>");
                $('#inspectSourceElementDialog').dialog('open');
                // highlight the element in red
                var obj = cs.current_highlight; // e.target;
                var pos = $(obj).offset();
                // console.log(pos);

                var ht = $(obj).height();
                var wd = $(obj).width();
                // global
                if (ss) {
                    ss.clear();
                }
                ss = new selectorHL(src_body,pos.top,pos.left,ht,wd,4,'red','fixed');
                currentDeliveranceRule.contentRule = selector;
                return false;
        });
        
        $(src_body).mouseover(
            function(e) {
                e.stopImmediatePropagation();
                var obj = e.target;
                if ($(e.target).hasClass('hover_selector_side')) {
                    return;
                }
                if (cs.current_highlight && cs.current_highlight != obj) {
                    if (cs.currentSel) {
                        cs.currentSel.clear();
                    }
                }
       
                var pos = $(obj).offset();
                
                var ht = $(obj).height();
                var wd = $(obj).width();

                cs.currentSel = new selectorHL(src_body,pos.top,pos.left,ht,wd,4,'#ff0','hover');
                // cs.currentSel = sel;
                cs.current_highlight = obj;
            }
        ); 

	window.src_body = src_body;
    });

    $('#delivtarget').load(function() {
        $(this).contents().find(".clickable").click(function(e) {
            e.stopPropagation();
            // get some sort of css selector based around the html id.
            var obj = this;
            // for selecting uls via li? need to use "ancestors"
            // if ($(this)[0].tagName.toLowerCase() === 'li') {
            //    obj = obj.parent();
            // }
            var selector = getCSSSelector($(obj));
            $('#status').html($('#status').html() + "Target: " + selector + "<br/>");
            // parent = getCSSSelector($(this).parent());
            // highlight the element in red
            var pos = $(obj).offset();
            var ht = $(obj).height();
            var wd = $(obj).width();
            // global
            if (ts) {
                ts.clear();
            }
            ts = new selectorHL(obj,pos.top,pos.left,ht,wd,4,'red', "TARGET_");

            if (currentDeliveranceRule && currentDeliveranceRule.contentRule != "") {
                currentDeliveranceRule.themeRule = selector;
                var rule = currentDeliveranceRule.toDeliveranceXML();
                rules.addRule({'action':'replace','content':currentDeliveranceRule.contentRule,'theme':currentDeliveranceRule.themeRule});
                $('#status').html("Rule added<br/>");
                    // ghetto escape it
                // $('#rules').html(rules.toXMLString("<br/>"));
                ts.fade();
                ss.fade();
                addRule();
            } else {
                $('#status').html($('#status').html() + 'No content rule yet<br/>')
            }
            return false;
	    });
        var theme_body = $(this).contents().find("body");
	$(theme_body).mouseover(
            function(e) {
                e.stopImmediatePropagation();
                var obj = e.target;
                if ($(e.target).hasClass('hover_selector_side')) {
                    return;
                }
                if (cs.current_highlight && cs.current_highlight != obj) {
                    if (cs.currentSel) {
                        cs.currentSel.clear();
                    }
                }
       
                var pos = $(obj).offset();
                
                var ht = $(obj).height();
                var wd = $(obj).width();

                cs.currentSel = new selectorHL(theme_body,pos.top,pos.left,ht,wd,4,'#f0f','hover');
                // cs.currentSel = sel;
                cs.current_highlight = obj;
            }
	);						
    });
});