/* collapsed_stacked_inlines.js */
/* Created in May 2009 by Hannes Rydén */
/* Use, distribute and modify freely */

// Original script
// https://djangosnippets.org/snippets/1492/

// 2021 updates by Dimitris Karagiannis
// @MitchKarajohn

jQuery(function ($) {
    var linkStyle =
      'cursor: pointer; color: #fff; border-radius: 4px; font-weight: 400; padding: 5px 10px; background: #417690; border: none;';
    
    // Only for stacked inlines
    $('div.inline-group div.inline-related:not(.tabular)').each(function () {
      const $h3 = $(this.querySelector('h3'));
      const $fs = $(this.querySelector('fieldset'));
      const fsErrorsExist = $fs.children('.errors').length;
      const initialButtonText = fsErrorsExist ? gettext('Hide') : gettext('Show');
      const $button = $(
        $.parseHTML(
          '<a role="button" style="' +
            linkStyle +
            '" class="stacked_collapse-toggle">' +
            initialButtonText +
            '</a> '
        )
      );
  
      // Don't collapse initially if fieldset contains errors
      if (fsErrorsExist) $fs.addClass('stacked_collapse');
      else $fs.addClass('stacked_collapse collapsed');
  
      // Add toggle link
      $button.click(function () {
        if (!$fs.hasClass('collapsed')) {
          $fs.addClass('collapsed');
          this.innerHTML = gettext('Show');
        } else {
          $fs.removeClass('collapsed');
          this.innerHTML = gettext('Hide');
        }
      });
  
      $h3.prepend($button);
    });
  });