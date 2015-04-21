/*global window:false, setTimeout:true, console:true */

(function(context) {
    'use strict';
    var win = context, doc = win.document;
    var research_form = $('#research_form');
    var form_steps = [];
    var source = doc.domain;
    var cookie_hide_name = "hide_dc_research";
    var cookie_name = "dc_research";
    research_form.hide()

    var Cookies = {
      get: function (key) {
          return decodeURIComponent(doc.cookie.replace(new RegExp('(?:(?:^|.*;)\\s*' + encodeURIComponent(key).replace(/[\-\.\+\*]/g, '\\$&') + '\\s*\\=\\s*([^;]*).*$)|^.*$'), '$1')) || null;
      },
      set: function (key, val, end, path, domain, secure) {
          if (!key || /^(?:expires|max\-age|path|domain|secure)$/i.test(key)) {
              return false;
          }
          var expires = '';
          if (end) {
              switch (end.constructor) {
                  case Number:
                      expires = end === Infinity ? '; expires=Fri, 31 Dec 9999 23:59:59 GMT' : '; max-age=' + end;
                      break;
                  case String:
                      expires = '; expires=' + end;
                  break;
                  case Date:
                      expires = '; expires=' + end.toUTCString();
                  break;
              }
          }
          doc.cookie = encodeURIComponent(key) + '=' + encodeURIComponent(val) + expires + (domain ? '; domain=' + domain : '') + (path ? '; path=' + path : '') + (secure ? '; secure' : '');
          return true;
        },
        has: function (key) {
            return (new RegExp('(?:^|;\\s*)' + encodeURIComponent(key).replace(/[\-\.\+\*]/g, '\\$&') + '\\s*\\=')).test(doc.cookie);
        },
        remove: function (key, path, domain) {
            if (!key || !this.has(key)) { return false; }
            doc.cookie = encodeURIComponent(key) + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT' + ( domain ? '; domain=' + domain : '') + ( path ? '; path=' + path : '');
            return true;
        }
    };

    function make_guid() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
          var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
          return v.toString(16);
      });
    }

    function load_fieldsets() {
      research_form.find('.research_step').each(function(n, el) {
        form_steps.push(el)
        $(el).find('button').on('click', post_answer);
      })
    }

    function show_step(step) {
      $.modal.close();

      var options = {
        onClose: function(dialog) {
          Cookies.set(cookie_hide_name, 1, Infinity, '/');
          $.modal.close();
        },
        autoPosition: false,
        closeHTML: "<a href='#' style='float:left' title='Close' class='modal-close'>Don't ask me again</a>",
        close: false,
        overlayClose: true,
        overlayCss: {
                'background-color':'#000',
        },
        containerCss: {
                'background-image':"url('https://democracyclub.org.uk/static/images/logo.png')",
                'background-repeat': 'no-repeat',
                'background-position': '2% 1em',
                'padding-left': '150px',
                'background-color':'#000',
                'color':'#FFF',
                'position':'fixed',
                'bottom':'0',
                'top':'auto !important',
                'max-width':'100%',
                'width':'100%',
                'height':'250px',
                'box-sizing': 'border-box'
          }
      }

      if (step == 0) {
        options['close'] = true;
      }

      $(form_steps[step]).modal(options);
    }

    function post_answer(el) {
      var data = {
        source: source,
        answer_set: window.guid,
        question: $(el.target).data('question')
      }
      var answer_el = $(el.target).data('answer_el');
      if (answer_el) {
        var answer = $('#' + answer_el).value();
      } else {
        var answer = $(el.target).attr('value') || $(el.target).text()
      }
      data['answer'] = answer;
      jQuery.post(
        'https://democracyclub.org.uk/research/answers/',
        data,
        function() {show_step(1);}
      )
    }

    function show_research_form() {


      // Work out if we should show the form
      if (!Cookies.has(cookie_hide_name)) {
        // Set a GUID
        if (!Cookies.has(cookie_name)) {
          var guid = make_guid();
          Cookies.set(cookie_name, guid, Infinity, '/');
        } else {
          var guid = Cookies.get(cookie_name);
        }
        window.guid = guid;
        load_fieldsets()
        show_step(0)
      }
    }

    function track_page_views() {
      var pageviews = parseInt(localStorage.getItem('pageviews')) || 0;
      localStorage.setItem('pageviews', pageviews+1)
      return pageviews;
    }

    var pageviews = track_page_views();
    if (pageviews > 2) {
      show_research_form();
    }

})(window);