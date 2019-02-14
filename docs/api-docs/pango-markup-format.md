# Pango Markup Format

Pango markup format can be used to format simple string with markup. The pango markup language is a very simple SGML-like language that allows you specify attributes with the text they are applied to by using a small set of markup tags. 

Using the pango markup language to markup text and parsing the result with the [`pango.parse_markup()`](https://developer.gnome.org/pygtk/stable/class-pangoattrlist.html#function-pango--parse-markup) function is a convenient way to generate the [`pango.AttrList`](https://developer.gnome.org/pygtk/stable/class-pangoattrlist.html) and plain text that can be used in a [`pango.Layout`](https://developer.gnome.org/pygtk/stable/class-pangolayout.html).

## Root tag

The root tag of a marked-up document is `#!html <markup>`, but the [`pango.parse_markup()`](https://developer.gnome.org/pygtk/stable/class-pangoattrlist.html#function-pango--parse-markup) function allows you to omit this tag, so you will most likely never need to use it.

## `#!html <span>` tag
The most general markup tag is `#!html <span>`. The `#!html <span>` tag has the following attributes:

`#!css font`[^1], `#!css font_desc`
:   A font description string, such as `Sans Italic 12`. See `pango_font_description_from_string()` for a description of the format of the string representation.

!!! note
    Any other span attributes will override this description. So if you have `Sans Italic` and also a `style="normal"` attribute, you will get `Sans normal`, not `italic`.

`#!css font_family`, `#!css face`
:   A font family name

`#!css font_size`[^1], `#!css size`
:   Font size in 1024ths of a point, or one of the absolute sizes `xx-small`, `x-small`, `small`, `medium`, `large`, `x-large`, `xx-large`, or one of the relative sizes `smaller` or `larger`. If you want to specify a absolute size, it's usually easier to take advantage of the ability to specify a partial font description using `font`. you can use `font="12.5"` rather than `size="12800"`.

`#!css font_style`[^1], `#!css style`
:   One of `normal`, `oblique`, `italic`

`#!css font_weight`[^1], `#!css weight`
:   One of `ultralight`, `light`, `normal`, `bold`, `ultrabold`, `heavy`, or a numeric weight

`#!css font_variant`[^1], `#!css variant`
:   One of `normal` or `smallcaps`

`#!css font_stretch`[^1], `#!css stretch`
:   One of `ultracondensed`, `extracondensed`, `condensed`, `semicondensed`, `normal`, `semiexpanded`, `expanded`, `extraexpanded`, `ultraexpanded`

`#!css font_features`[^2]
:   A comma separated list of OpenType font feature settings, in the same syntax as accepted by CSS. E.g: `#!html font_features="dlig=1, -kern, afrc on"`

`#!css foreground`, `#!css fgcolor`[^1], `#!css color`
:   An RGB color specification such as `#!css #00FF00` or a color name such as `red`. Since 1.38, an RGBA color specification such as `#!css #00FF007F` will be interpreted as specifying both a foreground color and foreground alpha.

`#!css background`, `#!css bgcolor`[^1]
:   An RGB color specification such as `#!css #00FF00` or a color name such as `red`. Since 1.38, an RGBA color specification such as `#!css #00FF007F` will be interpreted as specifying both a background color and background alpha.

`#!css alpha`, `#!css fgalpha`[^2]
:   An alpha value for the foreground color, either a plain integer between 1 and 65536 or a percentage value like `#!css 50%`.

`#!css background_alpha`, `#!css bgalpha`[^2]
:   An alpha value for the background color, either a plain integer between 1 and 65536 or a percentage value like `#!css 50%`.

`#!css underline`
:   One of `none`, `single`, `double`, `low`, `error`

`#!css underline_color`
:   The color of underlines; an RGB color specification such as `#!css #00FF00` or a color name such as `red`

`#!css rise`
:   Vertical displacement, in Pango units. Can be negative for subscript, positive for superscript.

`#!css strikethrough`
:   `#!css true` or `#!css false` whether to strike through the text

`#!css strikethrough_color`
:   The color of strikethrough lines; an RGB color specification such as `#!css #00FF00` or a color name such as `#!css red`

`#!css fallback`
:   `#!css true` or `#!css false` whether to enable fallback. If disabled, then characters will only be used from the closest matching font on the system. No fallback will be done to other fonts on the system that might contain the characters in the text. Fallback is enabled by default. Most applications should not disable fallback.

`#!css lang`
:   A language code, indicating the text language

`#!css letter_spacing`
:   Inter-letter spacing in 1024ths of a point.

`#!css gravity`
:   One of `south`, `east`, `north`, `west`, `auto`.

`#!css gravity_hint`
:   One of `natural`, `strong`, `line`.


## Other Supported tags

`#!html <b>`
:   Bold

`#!html <big>`
:   Makes font relatively larger, equivalent to `#!html <span size="larger">`

`#!html <i>`
:   Italic

`#!html <s>`
:   Strikethrough

`#!html <sub>`
:   Subscript

`#!html <sup>`
:   Superscript

`#!html <small>`
:   Makes font relatively smaller, equivalent to `#!html <span size="smaller">`

`#!html <tt>`
:   Monospace font

`#!html <u>`
:   Underline

`#!html <a>` (Not documented but it works)
:   to add a link in document i.e.,

```html
<a href="https://google.com" title="Open Google">Google</a>
```


[^1]: Since 1.21
[^2]: Since 1.38