
;(function (global) {
  'use strict'

  var $ = global.jQuery
  var DC = global.DC || {}
  DC.Modules = DC.Modules || {}

  DC.modules = {
    find: function (container) {
      container = container || $('body')

      var modules
      var moduleSelector = '[data-module]'

      modules = container.find(moduleSelector)

      // Container could be a module too
      if (container.is(moduleSelector)) {
        modules = modules.add(container)
      }

      return modules
    },

    start: function (container) {
      var modules = this.find(container)

      for (var i = 0, l = modules.length; i < l; i++) {
        var module
        var element = $(modules[i])
        var type = camelCaseAndCapitalise(element.data('module'))
        var started = element.data('module-started')

        if (typeof DC.Modules[type] === 'function' && !started) {
          module = new DC.Modules[type]()
          module.start(element)
          element.data('module-started', true)
        }
      }

      // eg selectable-table to SelectableTable
      function camelCaseAndCapitalise (string) {
        return capitaliseFirstLetter(camelCase(string))
      }

      // http://stackoverflow.com/questions/6660977/convert-hyphens-to-camel-case-camelcase
      function camelCase (string) {
        return string.replace(/-([a-z])/g, function (g) {
          return g[1].toUpperCase()
        })
      }

      // http://stackoverflow.com/questions/1026069/capitalize-the-first-letter-of-string-in-javascript
      function capitaliseFirstLetter (string) {
        return string.charAt(0).toUpperCase() + string.slice(1)
      }
    }
  }

  global.DC = DC
})(window)






// FORMS
;(function (global) {
  'use strict'
  var $ = global.jQuery
  var DC = global.DC || {}

  var SelectionButtons = function (elmsOrSelector, opts) {
    this.selectedClass = 'selected'
    this.focusedClass = 'focused'
    this.radioClass = 'selection-button-radio'
    this.checkboxClass = 'selection-button-checkbox'
    if (opts !== undefined) {
      $.each(opts, function (optionName, optionObj) {
        this[optionName] = optionObj
      }.bind(this))
    }
    if (typeof elmsOrSelector === 'string') {
      this.selector = elmsOrSelector
      this.setInitialState($(this.selector))
    } else if (elmsOrSelector !== undefined) {
      this.$elms = elmsOrSelector
      this.setInitialState(this.$elms)
    }
    this.addEvents()
  }

  SelectionButtons.prototype.addEvents = function () {
    if (typeof this.$elms !== 'undefined') {
      this.addElementLevelEvents()
    } else {
      this.addDocumentLevelEvents()
    }
  }
  SelectionButtons.prototype.setInitialState = function ($elms) {
    $elms.each(function (idx, elm) {
      var $elm = $(elm)

      var labelClass = $elm.attr('type') === 'radio' ? this.radioClass : this.checkboxClass
      $elm.parent('label').addClass(labelClass)
      if ($elm.is(':checked')) {
        this.markSelected($elm)
      }
    }.bind(this))
  }
  SelectionButtons.prototype.markFocused = function ($elm, state) {
    if (state === 'focused') {
      $elm.parent('label').addClass(this.focusedClass)
    } else {
      $elm.parent('label').removeClass(this.focusedClass)
    }
  }
  SelectionButtons.prototype.markSelected = function ($elm) {
    var radioName

    if ($elm.attr('type') === 'radio') {
      radioName = $elm.attr('name')
      $($elm[0].form).find('input[name="' + radioName + '"]')
        .parent('label')
        .removeClass(this.selectedClass)
      $elm.parent('label').addClass(this.selectedClass)
    } else { // checkbox
      if ($elm.is(':checked')) {
        $elm.parent('label').addClass(this.selectedClass)
      } else {
        $elm.parent('label').removeClass(this.selectedClass)
      }
    }
  }
  SelectionButtons.prototype.addElementLevelEvents = function () {
    this.clickHandler = this.getClickHandler()
    this.focusHandler = this.getFocusHandler({ 'level': 'element' })

    this.$elms
      .on('click', this.clickHandler)
      .on('focus blur', this.focusHandler)
  }
  SelectionButtons.prototype.addDocumentLevelEvents = function () {
    this.clickHandler = this.getClickHandler()
    this.focusHandler = this.getFocusHandler({ 'level': 'document' })

    $(document)
      .on('click', this.selector, this.clickHandler)
      .on('focus blur', this.selector, this.focusHandler)
  }
  SelectionButtons.prototype.getClickHandler = function () {
    return function (e) {
      this.markSelected($(e.target))
    }.bind(this)
  }
  SelectionButtons.prototype.getFocusHandler = function (opts) {
    var focusEvent = (opts.level === 'document') ? 'focusin' : 'focus'

    return function (e) {
      var state = (e.type === focusEvent) ? 'focused' : 'blurred'

      this.markFocused($(e.target), state)
    }.bind(this)
  }
  SelectionButtons.prototype.destroy = function () {
    if (typeof this.selector !== 'undefined') {
      $(document)
        .off('click', this.selector, this.clickHandler)
        .off('focus blur', this.selector, this.focusHandler)
    } else {
      this.$elms
        .off('click', this.clickHandler)
        .off('focus blur', this.focusHandler)
    }
  }

  DC.SelectionButtons = SelectionButtons
  global.DC = DC
})(window)


// ;$(document).foundation();
$(document).ready(function(){
    DC.modules.start()
    var selectionButtons = new DC.SelectionButtons("label input[type='radio'], label input[type='checkbox']")
});
