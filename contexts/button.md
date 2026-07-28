---
realComponent: ion-button
description: Angular standalone button component with design system styling and Shadow DOM encapsulation
themes: [modern-light-ds, modern-dark-ds]
props:
  - name: label
    type: string
    category: content
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: ariaLabel
    type: string
    category: accessibility
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: wrapLabel
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: icon
    type: string | IIconOptions
    category: visual
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: iconPlacement
    type: enum
    category: visual
    required: false
    default: "start"
    values: [start, end]
    designTokens: {}
  - name: size
    type: enum
    category: visual
    required: false
    default: "md"
    values: [xs, sm, md, lg]
    designTokens: {}
  - name: emphasis
    type: enum
    category: visual
    required: false
    default: "bold"
    values: [bold, moderate, subtle]
    designTokens:
      bold:
        light:
          resolvesTo: "#007de0"
          tokenChain: "primary bold background color -> --ion-lit-color-leonardo-base-primary (#007de0)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#007de0"
          tokenChain: "primary bold background color -> --ion-lit-color-leonardo-base-primary (#007de0)"
          appliesToCssProperty: "background-color"
      moderate:
        light:
          resolvesTo: "#e2eaff"
          tokenChain: "primary moderate background color -> --ion-lit-color-palette-light-blue-200 (#e2eaff)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#e2eaff"
          tokenChain: "primary moderate background color -> --ion-lit-color-palette-light-blue-200 (#e2eaff)"
          appliesToCssProperty: "background-color"
      subtle:
        light:
          resolvesTo: "#ffffff"
          tokenChain: "primary subtle background color -> white (#ffffff)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#ffffff"
          tokenChain: "primary subtle background color -> white (#ffffff)"
          appliesToCssProperty: "background-color"
  - name: intent
    type: enum
    category: visual
    required: false
    default: "primary"
    values: [primary, secondary, negative, positive, buy, sell, inverse, on-light, on-dark]
    designTokens:
      primary:
        light:
          resolvesTo: "#007de0"
          tokenChain: "primary intent background color -> --ion-lit-color-leonardo-base-primary (#007de0)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#007de0"
          tokenChain: "primary intent background color -> --ion-lit-color-leonardo-base-primary (#007de0)"
          appliesToCssProperty: "background-color"
      secondary:
        light:
          resolvesTo: "#030f26"
          tokenChain: "secondary intent background color -> --ion-lit-color-leonardo-base-secondary (#030f26)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#030f26"
          tokenChain: "secondary intent background color -> --ion-lit-color-leonardo-base-secondary (#030f26)"
          appliesToCssProperty: "background-color"
      negative:
        light:
          resolvesTo: "#c70000"
          tokenChain: "negative intent background color -> --ion-lit-color-leonardo-base-negative (#c70000)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#c70000"
          tokenChain: "negative intent background color -> --ion-lit-color-leonardo-base-negative (#c70000)"
          appliesToCssProperty: "background-color"
      positive:
        light:
          resolvesTo: "#2dc168"
          tokenChain: "positive intent background color -> --ion-lit-color-leonardo-base-positive (#2dc168)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#2dc168"
          tokenChain: "positive intent background color -> --ion-lit-color-leonardo-base-positive (#2dc168)"
          appliesToCssProperty: "background-color"
      buy:
        light:
          resolvesTo: "#007de0"
          tokenChain: "buy intent background color -> --ion-lit-color-leonardo-base-buy (#007de0)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#007de0"
          tokenChain: "buy intent background color -> --ion-lit-color-leonardo-base-buy (#007de0)"
          appliesToCssProperty: "background-color"
      sell:
        light:
          resolvesTo: "#c70000"
          tokenChain: "sell intent background color -> --ion-lit-color-leonardo-base-sell (#c70000)"
          appliesToCssProperty: "background-color"
        dark:
          resolvesTo: "#c70000"
          tokenChain: "sell intent background color -> --ion-lit-color-leonardo-base-sell (#c70000)"
          appliesToCssProperty: "background-color"
  - name: loading
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: disabled
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
  - name: loadingIcon
    type: string
    category: visual
    required: false
    default: "loading"
    values: []
    designTokens: {}
  - name: width
    type: string
    category: visual
    required: false
    default: "auto"
    values: []
    designTokens: {}
  - name: focus
    type: function
    category: behavioral
    required: false
    default: "() => this.buttonEl.nativeElement.focus()"
    values: []
    designTokens: {}
jointTokens:
  - combination: "intent=primary, emphasis=bold"
    resolvesTo: "#007de0"
    tokenChain: "component background -> --ion-comp-button-container-color-bg-primary-enabled-bold -> --ion-lit-color-leonardo-base-primary (#007de0)"
    appliesToCssProperty: "background-color"
  - combination: "intent=secondary, emphasis=bold"
    resolvesTo: "#030f26"
    tokenChain: "component background -> --ion-comp-button-container-color-bg-secondary-enabled-bold -> --ion-lit-color-leonardo-base-secondary (#030f26)"
    appliesToCssProperty: "background-color"
  - combination: "intent=positive, emphasis=bold"
    resolvesTo: "#2dc168"
    tokenChain: "component background -> --ion-comp-button-container-color-bg-positive-enabled-bold -> --ion-lit-color-leonardo-base-positive (#2dc168)"
    appliesToCssProperty: "background-color"
  - combination: "intent=negative, emphasis=bold"
    resolvesTo: "#c70000"
    tokenChain: "component background -> --ion-comp-button-container-color-bg-negative-enabled-bold -> --ion-lit-color-leonardo-base-negative (#c70000)"
    appliesToCssProperty: "background-color"
  - combination: "intent=buy, emphasis=bold"
    resolvesTo: "#007de0"
    tokenChain: "component background -> --ion-comp-button-container-color-bg-buy-enabled-bold -> --ion-lit-color-leonardo-base-buy (#007de0)"
    appliesToCssProperty: "background-color"
  - combination: "intent=sell, emphasis=bold"
    resolvesTo: "#c70000"
    tokenChain: "component background -> --ion-comp-button-container-color-bg-sell-enabled-bold -> --ion-lit-color-leonardo-base-sell (#c70000)"
    appliesToCssProperty: "background-color"
propInteractions:
  - loading spinner colors dynamically set via --button-spinner-indicator-color and --button-spinner-track-color custom properties based on intent and emphasis combination (e.g. --ion-comp-button-progress-indicator-indicator-color-bg-primary-bold)
  - wrapLabel controls whether text wraps to multiple lines or is truncated with ellipsis
  - iconPlacement changes which side of label icon renders on (start or end) but does not affect overall button dimensions
  - width prop sets inline display style and applies custom width, overrides default auto width behavior
  - disabled state suppresses loading spinner even when loading=true
  - size supports MQ design strings parsed by MqDesignStringParserService for responsive sizing (e.g. xs=sm;sm=md;md=md;lg=lg;xl=lg;xxl=md)
  - showSpinner property controls loading indicator visibility based on loading && !disabled condition
  - icon can be string or IIconOptions object; when string, uses legacy format "family name" that gets parsed into separate name and family properties
  - emphasis influences both background color and label/icon color through different token chains
needsReview:
  - No design token data found for intent values: inverse, on-light, on-dark (only primary, secondary, negative, positive, buy, sell traced from ds_tokens.css)
  - Dark theme tokens not fully traced for all intent/emphasis combinations - only primary intent tokens found; other intents may have dark theme variants not documented in provided ds_tokens.css
  - Color values for emphasis=moderate and emphasis=subtle combinations with different intents not traced from actual token definitions - only primary intent values documented
  - Label/icon color tokens not fully traced for all state combinations (hover, pressed, disabled) across all intents
  - Focus ring color tokens not traced from provided token files
  - Dark theme background colors may differ from light theme but not all combinations verified in provided ds_tokens.css
  - CSS custom properties for loading spinner colors (--ion-comp-button-progress-indicator-indicator-color-bg-*, --ion-comp-button-progress-indicator-track-color-bg-*) not traced to final resolved values
  - Dark theme variations for leonardo base colors present in ds_tokens.css but component-specific token chains not fully accessible without complete token resolution
  - Intent-specific color behavior for on-light and on-dark intents appears to use different token system (base toggle) but token values not traced
  - MQ design string parsing results not verifiable without runtime screen size context - defaults to md when MQ strings used
  - Color tokens for emphasis=moderate and emphasis=subtle with non-primary intents (secondary, negative, positive, buy, sell) not traced from provided files
---

## label

Controls the button text content. When empty, button may render as icon-only or with no visible content (for purely decorative or icon-based buttons). This prop drives the showLabel template property which determines whether the label element is rendered in the template.

**Visual cues:**
- When set, displays text in button center with styling determined by intent and emphasis
- When empty, button may still function as icon-only if icon is provided, or as structural element if neither label nor icon present

**When to use:**
- Primary method for conveying button purpose through text
- Should be omitted for purely icon-based buttons where icon alone conveys meaning
- Falls back to empty string if falsy value provided

## ariaLabel

Provides accessibility label for screen readers and assistive technologies. This is not derivable from a visual design and should generally be left at its default unless the developer's request specifically calls for it.

**Default behavior:**
- Uses label value as fallback if ariaLabel not explicitly set
- Falls back to icon name if neither label nor ariaLabel provided
- Returns "No label" as last resort

**Visual property:** none (accessibility-only)

## wrapLabel

Controls whether button label text wraps to multiple lines or stays on single line.

**Visual cues:**
- true: Text wraps to multiple lines if longer than button width
- false: Text may be truncated with ellipsis beyond container (default behavior)

**When to use:**
- Set true for buttons with potentially long, variable-length text
- Keep false for consistent button dimensions with shorter text

## icon

Controls icon display as prefix or suffix to button text. Accepts either string (legacy format "family name") or IIconOptions object with separate name and family properties.

**Visual cues:**
- String format: Uses legacy format that gets parsed via parseIconName() and parseFamilyName() utilities
- Object format: More precise control with explicit name and family properties
- Icon visibility controlled by showStartIcon/showEndIcon computed properties based on iconPlacement
- When empty, button renders text-only (or structural element if label also empty)

**When to use:**
- String: Legacy compatibility when icon family and name are space-separated
- Object: New API when separate control over icon name and family needed
- Empty: Text-only button

## iconPlacement

Controls which side of the label the icon renders on.

**Visual cues:**
- start: Icon appears to left of label
- end: Icon appears to right of label

**When to use:**
- start: Most common standard pattern for primary actions
- end: Use for patterns where icon is more important than text or for right-to-left layout preferences

**Legacy compatibility:**
- Automatically maps legacy `before` value to `start`
- Automatically maps legacy `after` value to `end`

## size

Controls button sizing both through direct enum values and responsive MQ design strings.

**Visual cues:**
- xs: Extra small button, used for compact layouts or icon-only buttons
- sm: Small button, moderate compact sizing
- md: Medium button (default), standard sizing
- lg: Large button, prominent sizing

**When to use:**
- xs: Navigation toolbars, action bars with space constraints
- sm: Secondary action groups, form actions with limited space
- md: Primary actions, standard buttons (default)
- lg: Primary call-to-action buttons, promotional content

**Responsive behavior:**
- Supports MQ design strings parsed by MqDesignStringParserService
- Returns default "md" if invalid size string provided
- Example MQ string: xs=sm;sm=md;md=md;lg=lg;xl=lg;xxl=md

## emphasis

Controls visual weight and prominence of the button through color and fill variations.

**Visual cues:**
- bold: Solid fill with full color background (default)
- moderate: Lighter background fill with more subtle color
- subtle: Minimal fill, often white or transparent background with colored border

**When to use:**
- bold: Most important primary action in a group
- moderate: Secondary actions, less prominent but still important
- subtle: Tertiary actions, inverse buttons, or when button needs to be less visually dominant

**Color behavior:**
- Single prop influences both background-color andforeground color for label and icon
- Combined with intent to determine final color values
- Color values depend on combination with intent property (see jointTokens)

## intent

Controls semantic meaning and color scheme of the button for different action types.

**Visual cues:**
- primary: Blue (#007de0), default primary actions
- secondary: Dark navy (#030f26), important but not primary actions
- negative: Red (#c70000), destructive or error-related actions
- positive: Green (#2dc168), success or confirm actions
- buy: Blue (#007de0), trade buy actions
- sell: Red (#c70000), trade sell actions
- inverse: For use on dark backgrounds (not fully traced)
- on-light: For use on light backgrounds (not fully traced)
- on-dark: For use on dark backgrounds (not fully traced)

**When to use:**
- primary: Main action in a feature or page
- secondary: Actions that are important but not the primary action
- negative: Destructive actions like delete, cancel, or error-related actions
- positive: Success actions like confirm, save, or complete
- buy/sell: Trading-specific actions in financial applications
- inverse/on-light/on-dark: Context-specific usage depending on background color

**Color behavior:**
- Each intent has specific base colors defined in ds_tokens.css
- Combined with emphasis to determine final applied color
- Affects both button container and foreground (label/icon) colors

## loading

Controls loading state display, showing spinner when true and disabled is false.

**Visual cues:**
- When true: Shows loading spinner in button center, replacing or overlaying content
- Spinner size controlled by getSpinnerClass() based on button size
- Spinner colors dynamically set via CSS custom properties based on intent and emphasis

**When to use:**
- Set true during async operations like form submission, API calls, or data fetching
- Spinner only shows when loading=true AND disabled=false
- Automatically manages spinner visibility through showSpinner computed property

**Spinner color management:**
- Uses --button-spinner-indicator-color custom property referencing --ion-comp-button-progress-indicator-indicator-color-bg-{intent}-{emphasis}
- Uses --button-spinner-track-color custom property referencing --ion-comp-button-progress-indicator-track-color-bg-{intent}-{emphasis}
- These are temporary implementation notes until spinner widget migrates to DS

## disabled

Controls disabled state of the button, preventing interaction.

**Visual cues:**
- When true: Button appears non-interactive, typically with reduced opacity and disabled cursor
- Suppresses loading spinner even when loading=true
- Affects button styling through disabled CSS class

**When to use:**
- Set true when button action is not currently available
- Override default false when form validation fails or permission-based restrictions apply

## loadingIcon

Controls the icon name used for the loading spinner.

**Visual cues:**
- Uses specified icon name for spinner visualization
- Default "loading" icon provides standard spinner appearance
- Maps to icon system through IIconOptions or string format

**When to use:**
- Override default when custom loading icon needed
- Keep using default "loading" for consistent loading state visualization

## width

Controls button width for backward compatibility with legacy API.

**Visual cues:**
- Sets inline display style to block and applies custom width
- Supports various width formats: pixel values, percentages, CSS variables (prefixed with --)
- Special "full" value maps to "100%"

**When to use:**
- Only for backward compatibility with legacy width API
- New implementations should rely on standard width styling instead
- Set to CSS variable with "--" prefix to use design token value
- Set to "full" for full-width button

**Behavioral notes:**
- Overrides default auto width when set
- Applies styles directly to nativeElement
- Quick fix prevents redundant style application if width value unchanged

## focus

Provides programmatic focus override for the webcomponent button element.

**Visual property:** none (behavioral)

**When to use:**
- This is a behavioral prop not derivable from visual design
- Should generally be left at its default unless specifically called for in request
- Overrides default focus behavior for programmatic focus triggering
- Calls buttonEl.nativeElement.focus() when invoked

**Default behavior:**
- Function reference that focuses button element when called
- Resolves webcomponent focus issue where programmatic focus doesn't work correctly

## Examples

```html
<ion-button label="Primary Button" intent="primary" emphasis="bold">Primary Title</ion-button>
```
Demonstrates primary button with default bold emphasis and label text.

```html
<ion-button label="Secondary Button" intent="secondary" emphasis="bold">Secondary Title</ion-button>
```
Demonstrates secondary button with dark navy color for important but non-primary actions.

```html
<ion-button label="Positive Button" intent="positive" emphasis="bold">Positive Title</ion-button>
```
Demonstrates positive button with green color for success or confirm actions.

```html
<ion-button label="Negative Button" intent="negative" emphasis="bold">Negative Title</ion-button>
```
Demonstrates negative button with red color for destructive or error-related actions.

```html
<ion-button label="Buy Button" intent="buy" emphasis="bold">Buy Title</ion-button>
```
Demonstrates trading-specific buy action button with blue color.

```html
<ion-button label="Sell Button" intent="sell" emphasis="bold">Sell Title</ion-button>
```
Demonstrates trading-specific sell action button with red color.

```html
<ion-button label="Inverse Button" intent="inverse" emphasis="bold" hidden="!useDesignSystemTheme">Inverse Title</ion-button>
```
Demonstrates inverse button for use on dark backgrounds, conditionally hidden.

```html
<ion-button wrapLabel="wrapLabel" width="width" iconPlacement="iconPlacement" icon="customIcon || selectedIcon" intent="primary" disabled="disabled" size="size" emphasis="emphasis"></ion-button>
```
Demonstrates icon-only button configuration with potential wrap behavior, custom width, icon placement logic, and disabled state.
