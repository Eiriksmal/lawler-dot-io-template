Title: Banish the Firefox Megabar
Date: 2020-06-17 14:34
Category: Dross
Tags: software, reference
Description: Firefox makes it harder-than ever to customize their browser. Remove the Megabar with a userChrome CSS file.
Status: Published

<section markdown="1">
Mozilla continues the war against its own users in Firefox 77, disabling workarounds to their horrific "megabar" that were launched with the "feature" in Firefox 75. Kill it with fire with a custom user-defined CSS. Like it's 1997.

[UserChrome.org](https://www.userchrome.org/megabar-styling-firefox-address-bar.html) has the instructions for doing this *and* a fantastic CSS generator that can override a bunch of Mozilla's other new defaults. I didn't notice their other address bar-related changes, so this is a barebones `userChrome.css` that kills the Megabar and retains the changes they've made to the search dropdown in the past year.

Knowing link rot, that site will disappear and/or be impossible to find. I'll need to keep punting this file around for the next decade or so, so I'm saving it to this <del>blog</del><label for="mn-is-it-a-blog" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-is-it-a-blog" class="margin-toggle"><span class="marginnote">I think you have to write content to call a website a blog, right?</span> website for future reference.

This goes in a new folder named `chrome` in your current profile directory. eg `~/.mozilla/firefox/mlq5vmgg.default-release/chrome/userChrome.css`<label for="mn-nowyouknog" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-nowyouknog" class="margin-toggle"><span class="marginnote">...to use a totally hypothetical path.</span>
```css
/*** BEGIN Firefox 77 (June 2, 2020) Override URL bar enlargement ***/

  /* Compute new position, width, and padding */

  #urlbar[breakout][breakout-extend] {
    top: 5px !important;
    left: 0px !important;
    width: 100% !important;
    padding: 0px !important;
  }
  /* for alternate Density settings */
  [uidensity="compact"] #urlbar[breakout][breakout-extend] {
    top: 3px !important;
  }
  [uidensity="touch"] #urlbar[breakout][breakout-extend] {
    top: 4px !important;
  }

  /* Prevent shift of URL bar contents */

  #urlbar[breakout][breakout-extend] > #urlbar-input-container {
    height: var(--urlbar-height) !important;
    padding: 0 !important;
  }

  /* Do not animate */

  #urlbar[breakout][breakout-extend] > #urlbar-background {
    animation: none !important;;
  }

  /* Remove shadows */

  #urlbar[breakout][breakout-extend] > #urlbar-background {
    box-shadow: none !important;
  }

/*** END Firefox 77 (June 2, 2020) Override URL bar enlargement ***/
```

Once that's in the userChrome.css file... it still won't work. 😬 That's because Firefox 69 disabled the automatic search for, and loading of, the userChrome file. To finally be rid of the Megabar, ensure that `toolkit.legacyUserProfileCustomizations.stylesheets` configuration setting in your `about:config` is true. Restart Firefox and wave goodbye to that nasty blue monster.

</section>
