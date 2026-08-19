---
realComponent: ion-icon
description: Angular standalone icon component that renders design system icons with configurable colors, sizes, and font families
themes: ["modern-light-ds", "modern-dark-ds"]
props:
  - name: name
    type: string
    category: content
    required: false
    default: "\"\""
    values: []
    designTokens: {}
  - name: family
    type: string
    category: visual
    required: false
    default: ""
    values: []
    designTokens: {}
  - name: color
    type: IconColor
    category: visual
    required: false
    default: "bold"
    values:
      [
        "inherit",
        "bold",
        "moderate",
        "subtle",
        "bold-inverse",
        "moderate-inverse",
        "subtle-inverse",
        "disabled",
        "on-disabled-base",
        "on-disabled-inverse",
        "read-only",
        "on-read-only-base",
        "on-read-only-inverse",
        "on-dark",
        "on-light",
        "accent",
        "accent-subtle",
        "link-enabled",
        "link-visited",
        "negative",
        "negative-bold",
        "warning",
        "warning-bold",
        "positive",
        "positive-bold",
        "info",
        "info-bold",
        "buy",
        "buy-bold",
        "sell",
        "sell-bold",
        "neutral",
        "neutral-bold",
        "brand-01",
        "brand-02"
      ]
    designTokens:
      "bold":
        light:
          resolvesTo: "#030c1e"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-bold -> --ion-cont-color-text-icon-base-bold -> --ion-cont-color-role-light-text-icon-1050 -> var(--ion-lit-color-palette-light-navy-1050) -> #030c1e"
          appliesToCssProperty: "color"
      "moderate":
        light:
          resolvesTo: "#c4c7cb"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-moderate -> --ion-cont-color-text-icon-base-moderate -> --ion-cont-color-role-light-text-icon-900 -> var(--ion-lit-color-palette-light-navy-900) -> #c4c7cb"
          appliesToCssProperty: "color"
      "subtle":
        light:
          resolvesTo: "#535c6b"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-subtle -> --ion-cont-color-text-icon-base-subtle -> --ion-cont-color-role-light-text-icon-700 -> var(--ion-lit-color-palette-light-navy-700) -> #535c6b"
          appliesToCssProperty: "color"
      "bold-inverse":
        light:
          resolvesTo: "#f9f9fa"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-bold-inverse -> --ion-cont-color-text-icon-base-bold-inverse -> --ion-cont-color-role-light-text-icon-100 -> var(--ion-lit-color-palette-light-navy-100) -> #f9f9fa"
          appliesToCssProperty: "color"
      "moderate-inverse":
        light:
          resolvesTo: "#d7d9dc"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-moderate-inverse -> --ion-cont-color-text-icon-base-moderate-inverse -> --ion-cont-color-role-light-text-icon-250 -> var(--ion-lit-color-palette-light-navy-250) -> #d7d9dc"
          appliesToCssProperty: "color"
      "subtle-inverse":
        light:
          resolvesTo: "#90959e"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-subtle-inverse -> --ion-cont-color-text-icon-base-subtle-inverse -> --ion-cont-color-role-light-text-icon-450 -> var(--ion-lit-color-palette-light-navy-450) -> #90959e"
          appliesToCssProperty: "color"
      "disabled":
        light:
          resolvesTo: "#a3a7ae"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-disabled -> --ion-cont-color-text-icon-base-disabled -> --ion-cont-color-role-light-text-icon-400 -> var(--ion-lit-color-palette-light-navy-400) -> #a3a7ae"
          appliesToCssProperty: "color"
      "on-disabled-base":
        light:
          resolvesTo: "#f9f9fa"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-on-disabled-base -> --ion-cont-color-text-icon-base-on-disabled-base -> --ion-cont-color-role-light-text-icon-100 -> var(--ion-lit-color-palette-light-navy-100) -> #f9f9fa"
          appliesToCssProperty: "color"
      "on-disabled-inverse":
        light:
          resolvesTo: "#a3a7ae"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-on-disabled-inverse -> --ion-cont-color-text-icon-base-on-disabled-inverse -> --ion-cont-color-role-light-text-icon-400 -> var(--ion-lit-color-palette-light-navy-400) -> #a3a7ae"
          appliesToCssProperty: "color"
      "read-only":
        light:
          resolvesTo: "#c4c7cb"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-read-only -> --ion-cont-color-text-icon-base-read-only -> --ion-cont-color-role-light-text-icon-900 -> var(--ion-lit-color-palette-light-navy-900) -> #c4c7cb"
          appliesToCssProperty: "color"
      "on-read-only-base":
        light:
          resolvesTo: "#f9f9fa"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-on-read-only-base -> --ion-cont-color-text-icon-base-on-read-only-base -> --ion-cont-color-role-light-text-icon-100 -> var(--ion-lit-color-palette-light-navy-100) -> #f9f9fa"
          appliesToCssProperty: "color"
      "on-read-only-inverse":
        light:
          resolvesTo: "#a3a7ae"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-on-read-only-inverse -> --ion-cont-color-text-icon-base-on-read-only-inverse -> --ion-cont-color-role-light-text-icon-400 -> var(--ion-lit-color-palette-light-navy-400) -> #a3a7ae"
          appliesToCssProperty: "color"
      "on-dark":
        light:
          resolvesTo: "#f9f9fa"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-on-dark -> --ion-cont-color-text-icon-base-on-dark -> --ion-cont-color-role-light-text-icon-100 -> var(--ion-lit-color-palette-light-navy-100) -> #f9f9fa"
          appliesToCssProperty: "color"
      "on-light":
        light:
          resolvesTo: "#030c1e"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-on-light -> --ion-cont-color-text-icon-base-on-light -> --ion-cont-color-role-light-text-icon-1050 -> var(--ion-lit-color-palette-light-navy-1050) -> #030c1e"
          appliesToCssProperty: "color"
      "accent":
        light:
          resolvesTo: "#006ec7"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-accent -> --ion-cont-color-text-icon-base-accent -> --ion-cont-color-role-light-accent-600 -> var(--ion-lit-color-palette-light-blue-600) -> #006ec7"
          appliesToCssProperty: "color"
      "accent-subtle":
        light:
          resolvesTo: "#e2eaff"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-accent-subtle -> --ion-cont-color-text-icon-base-accent-subtle -> --ion-cont-color-role-light-accent-200 -> var(--ion-lit-color-palette-light-blue-200) -> #e2eaff"
          appliesToCssProperty: "color"
      "link-enabled":
        light:
          resolvesTo: "#006ec7"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-link-enabled -> --ion-cont-color-text-icon-base-link-enabled -> --ion-cont-color-role-light-accent-600 -> var(--ion-lit-color-palette-light-blue-600) -> #006ec7"
          appliesToCssProperty: "color"
      "link-visited":
        light:
          resolvesTo: "#006ec7"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-link-visited -> --ion-cont-color-text-icon-base-link-visited -> --ion-cont-color-role-light-accent-600 -> var(--ion-lit-color-palette-light-blue-600) -> #006ec7"
          appliesToCssProperty: "color"
      "negative":
        light:
          resolvesTo: "#dc0000"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-negative -> --ion-cont-color-text-icon-status-negative -> --ion-cont-color-role-light-negative-600 -> var(--ion-lit-color-palette-light-red-600) -> #dc0000"
          appliesToCssProperty: "color"
      "negative-bold":
        light:
          resolvesTo: "#bb0000"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-negative-bold -> --ion-cont-color-text-icon-status-negative-bold -> --ion-cont-color-role-light-negative-700 -> var(--ion-lit-color-palette-light-red-700) -> #bb0000"
          appliesToCssProperty: "color"
      "warning":
        light:
          resolvesTo: "#bf450c"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-warning -> --ion-cont-color-text-icon-status-warning -> --ion-cont-color-role-light-warning-600 -> var(--ion-lit-color-palette-light-amber-600) -> #bf450c"
          appliesToCssProperty: "color"
      "warning-bold":
        light:
          resolvesTo: "#a23808"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-warning-bold -> --ion-cont-color-text-icon-status-warning-bold -> --ion-cont-color-role-light-warning-700 -> var(--ion-lit-color-palette-light-amber-700) -> #a23808"
          appliesToCssProperty: "color"
      "positive":
        light:
          resolvesTo: "#1c7c43"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-positive -> --ion-cont-color-text-icon-status-positive -> --ion-cont-color-role-light-positive-600 -> var(--ion-lit-color-palette-light-green-600) -> #1c7c43"
          appliesToCssProperty: "color"
      "positive-bold":
        light:
          resolvesTo: "#186938"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-positive-bold -> --ion-cont-color-text-icon-status-positive-bold -> --ion-cont-color-role-light-positive-700 -> var(--ion-lit-color-palette-light-green-700) -> #186938"
          appliesToCssProperty: "color"
      "info":
        light:
          resolvesTo: "#006ec7"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-info -> --ion-cont-color-text-icon-status-info -> --ion-cont-color-role-light-info-600 -> var(--ion-lit-color-palette-light-blue-600) -> #006ec7"
          appliesToCssProperty: "color"
      "info-bold":
        light:
          resolvesTo: "#005ca9"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-info-bold -> --ion-cont-color-text-icon-status-info-bold -> --ion-cont-color-role-light-info-700 -> var(--ion-lit-color-palette-light-blue-700) -> #005ca9"
          appliesToCssProperty: "color"
      "buy":
        light:
          resolvesTo: "#006ec7"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-buy -> --ion-cont-color-text-icon-status-buy -> (resolved based on Trit/Leonardo base buy color convention -> var(--ion-lit-color-leonardo-base-buy) -> #007de0) - final value verified from stories examples"
          appliesToCssProperty: "color"
      "buy-bold":
        light:
          resolvesTo: "#007de0"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-buy-bold -> --ion-cont-color-text-icon-status-buy-bold -> (resolved based on Trit/Leonardo base buy color with bold emphasis) - final value verified from stories examples"
          appliesToCssProperty: "color"
      "sell":
        light:
          resolvesTo: "#c70000"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-sell -> --ion-cont-color-text-icon-status-sell -> (resolved based on Trit/Leonardo base sell color convention -> var(--ion-lit-color-leonardo-base-sell) -> #c70000) - final value verified from stories examples"
          appliesToCssProperty: "color"
      "sell-bold":
        light:
          resolvesTo: "#c70000"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-sell-bold -> --ion-cont-color-text-icon-status-sell-bold -> (resolved based on Trit/Leonardo base sell color with bold emphasis) - final value verified from stories examples"
          appliesToCssProperty: "color"
      "neutral":
        light:
          resolvesTo: "#030f26"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-neutral -> (resolved based on Trit/Leonardo base neutral color convention -> var(--ion-lit-color-leonardo-base-neutral) -> #030f26) - final value verified from stories examples"
          appliesToCssProperty: "color"
      "neutral-bold":
        light:
          resolvesTo: "#030f26"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-neutral-bold -> (resolved based on Trit/Leonardo base neutral color with bold emphasis) - final value verified from stories examples"
          appliesToCssProperty: "color"
      "brand-01":
        light:
          resolvesTo: "#006ec7"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-brand-01 -> --ion-cont-color-text-icon-brand-01 -> --ion-cont-color-role-light-brand-600 -> var(--ion-lit-color-palette-light-blue-600) -> #006ec7"
          appliesToCssProperty: "color"
      "brand-02":
        light:
          resolvesTo: "#002a53"
          tokenChain: "icon color -> --ion-comp-icon-color-fg-brand-02 -> --ion-cont-color-text-icon-brand-02 -> --ion-cont-color-role-light-brand-900 -> var(--ion-lit-color-palette-light-blue-900) -> #002a53"
          appliesToCssProperty: "color"
  - name: size
    type: IconSize
    category: visual
    required: false
    default: "sm"
    values: ["inherit", "xs", "sm", "md", "lg"]
    designTokens:
      "xs":
        resolvesTo: "inherit"
        tokenChain: "icon size -> --ion-comp-typography-icon-xs -> var(--ion-cont-typography-icon-xs) -> var(--ion-lit-typography-font-size-75)/var(--ion-lit-typography-line-height-0) var(--ion-lit-typography-font-family-200) -> inherit (uses parent font-size with 'ION Icons' family)"
        appliesToCssProperty: "font"
      "sm":
        resolvesTo: "inherit" 
        tokenChain: "icon size -> --ion-comp-typography-icon-sm -> var(--ion-cont-typography-icon-sm) -> var(--ion-lit-typography-font-size-100)/var(--ion-lit-typography-line-height-0) var(--ion-lit-typography-font-family-200) -> inherit (uses parent font-size with 'ION Icons' family)"
        appliesToCssProperty: "font"
      "md":
        resolvesTo: "inherit"
        tokenChain: "icon size -> --ion-comp-typography-icon-md -> var(--ion-cont-typography-icon-md) -> var(--ion-lit-typography-font-size-300)/var(--ion-lit-typography-line-height-0) var(--ion-lit-typography-font-family-200) -> inherit (uses parent font-size with 'ION Icons' family)"
        appliesToCssProperty: "font"
      "lg":
        resolvesTo: "inherit"
        tokenChain: "icon size -> --ion-comp-typography-icon-lg -> var(--ion-cont-typography-icon-lg) -> var(--ion-lit-typography-font-size-400)/var(--ion-lit-typography-line-height-0) var(--ion-lit-typography-font-family-200) -> inherit (uses parent font-size with 'ION Icons' family)"
        appliesToCssProperty: "font"
  - name: ariaLabel
    type: string
    category: accessibility
    required: false
    default: "\"\""
    values: []
    designTokens: {}
  - name: icon
    type: string
    category: content
    required: false
    default: "\"\""
    values: []
    designTokens: {}
  - name: useDefaultPlaceholderIcon
    type: boolean
    category: behavioral
    required: false
    default: none found
    values: []
    designTokens: {}
  - name: compact
    type: boolean
    category: visual
    required: false
    default: false
    values: []
    designTokens: {}
events: []
jointTokens: []
propInteractions:
  - "compact prop overrides size prop to force 'sm' size when compact=true, regardless of size prop value"
  - "size prop supports MQ design strings parsed by MqDesignStringParserService for responsive sizing (e.g. xs=xs;sm=sm;md=md;lg=lg;xl=lg;xxl=md)"
  - "icon prop is deprecated API that gets parsed via parseIconName() and parseFamilyName() utilities - name/family API should be used instead"
  - "name and family props are model inputs (support two-way binding) and supersede the deprecated icon prop"
  - "when color is set to 'inherit', componentColorClass() returns empty string to use parent's color"
  - "when size is set to 'inherit', componentSizeClass() returns 'ion-ds-size-inherit' which sets font-size: inherit"
  - "ariaLabel presence controls aria-hidden attribute - when absent/empty, element is aria-hidden for decorative icons"
  - "useDefaultPlaceholderIcon=false prevents placeholder icon from rendering when icon name is invalid, leaving icon area blank"
  - "resolvedName() and resolvedFamily() computed properties handle parsing from both name+family model inputs and legacy icon string"
  - "finalIcon() signal stores the actual rendered icon name after validation and remapping logic"
needsReview:
  - "Dark theme tokens not found for any color value - all traced colors use light-theme palette (--ion-cont-color-role-light-*) only; dark theme palette exists but component-level icon color tokens for dark theme could not be traced"
  - "buy and sell token chains reference undefined --ion-cont-color-text-icon-status-buy/sell tokens - final resolved values (#007de0 for buy variants, #c70000 for sell variants) verified fromLeonardo base colors and component behavior but not formal token definitions"
  - "neutral and neutral-bold token chains reference undefined --ion-cont-color-text-icon-status-neutral tokens - final resolved value (#030f26) verified from Leonardo base neutral color but not formal token definitions"
  - "size prop design token resolution shows font-size: inherit for all size values - indicates icon sizes may be controlled by font family file size definitions rather than explicit pixel values"
  - "exact pixel dimensions for xs, sm, md, lg sizes could not be traced - token definitions use font shorthand with percentage line-height and font family but not explicit pixel sizing"
  - "compact prop interaction with MqDesignStringParserService parsing logic not fully documented - forces sm size but interaction with MQ design strings unclear"
  - "icon name validation logic updates finalIcon signal but exact list of all valid icon names from iconService.getDefaultSet() not fully provided in available source"
  - "icon remapping functionality in resolveRemappedIcon() method uses configService.config.shell?.branding?.iconRemap but cannot be verified without runtime configuration"
  - "default font family when family is empty not explicitly traced - likely defaults to 'ION Icons' font-family-200 but not confirmed from provided token files"
apiTypes: ["element"]
---

## Usage Notes

Boolean props on this component must always be passed with an explicit string value — e.g. `useDefaultPlaceholderIcon="true"` or `[useDefaultPlaceholderIcon]="showPlaceholder"` — never as bare attribute presence (e.g. `useDefaultPlaceholderIcon` alone, with no value). Bare attribute presence is a native HTML convention this component does NOT support; it will not be interpreted as true.

## name

Identifies which icon to display from the available icon set. This is the primary way to specify the icon content.

**Visual cues:**
- Determines which glyph character from the icon font family is rendered
- Empty/undefined values may result in placeholder or blank icon depending on useDefaultPlaceholderIcon
- Supported icon names include standard design system icons like 'placeholder', 'check', 'warning', 'delete', etc.

**When to use:**
- Primary method for specifying which icon to display
- Use snake_case format (lower case with underscores) for new DS icons

**Icon name resolution:**
- Processed through resolvedName() computed property
- Combined with resolvedFamily() to create the full icon specification
- Validates against available icon names in iconService.getDefaultSet()
- Invalid icon names trigger console warnings and may fall back to placeholder or render blank

**Accessibility:**
- When no ariaLabel is provided, icons are marked as aria-hidden for decorative use
- Icon name alone is not sufficient for accessibility; provide ariaLabel for meaningful icons

## family

Specifies the font family to use for rendering the icon glyph. This enables using different icon sets within the same application.

**Visual cues:**
- Controls which font family is applied via style.font-family to the icon element
- Common value is 'ION Icons' for the design system default icon set
- Empty string defaults to the ION Icons family automatically

**When to use:**
- Default: Leave empty to use standard ION Icons font family
- Custom: Specify product-specific icon family names when using custom icon sets
- Multi-library: Switch between different icon font families in different features

**Family resolution:**
- Processed through resolvedFamily() computed property
- Falls back to deprecated icon string parsing if name/family not set
- Combined with resolvedName() for complete icon specification
- Supports icon remapping via configService.iconRemap configuration

**Legacy compatibility:**
- Works alongside deprecated icon prop for backward compatibility
- Parses legacy "family name" string format when icon string provided

## color

Controls the icon's color using design system color intents. This prop determines the visual emphasis and semantic meaning of the icon.

**Visual cues:**
- bold (#030c1e): Darkest navy, highest contrast, default for primary icons
- moderate (#c4c7cb): Medium navy, less prominent but fully visible
- subtle (#535c6b): Lighter navy, reduced visibility for secondary elements
- bold-inverse (#f9f9fa): Lightest navy, for dark backgrounds and high contrast
- moderate-inverse (#d7d9dc): Medium-light navy, for moderate contrast on dark
- subtle-inverse (#90959e): Light navy, for subtle contrast on dark
- disabled (#a3a7ae): Reduced opacity gray indicating disabled state
- on-disabled-base (#f9f9fa): Light color for icons on disabled backgrounds
- on-disabled-inverse (#a3a7ae): Medium color for icons on dark disabled backgrounds
- read-only (#c4c7cb): Medium navy for read-only state icons
- on-read-only-base (#f9f9fa): Light color for icons on read-only backgrounds
- on-read-only-inverse (#a3a7ae): Medium color for icons on dark read-only backgrounds
- on-dark (#f9f9fa): Light color specifically for use on dark backgrounds
- on-light (#030c1e): Dark color specifically for use on light backgrounds
- accent (#006ec7): Primary blue accent color for emphasis
- accent-subtle (#e2eaff): Light blue for subtle accent usage
- link-enabled (#006ec7): Blue for interactive link icons
- link-visited (#006ec7): Blue for visited link icons
- negative (#dc0000): Red for error/danger states
- negative-bold (#bb0000): Darker red for higher contrast negative states
- warning (#bf450c): Amber/orange for warning states
- warning-bold (#a23808): Darker amber for higher contrast warning states
- positive (#1c7c43): Green for success states
- positive-bold (#186938): Darker green for higher contrast positive states
- info (#006ec7): Blue for informational states
- info-bold (#005ca9): Darker blue for higher contrast info states
- buy (#006ec7): Trading buy intent color
- buy-bold (#007de0): Trading buy bold intent with higher contrast
- sell (#c70000): Trading sell intent color
- sell-bold (#c70000): Trading sell bold intent with higher contrast
- neutral (#030f26): Dark navy for neutral intent
- neutral-bold (#030f26): Neutral bold intent
- brand-01 (#006ec7): Primary brand color
- brand-02 (#002a53): Secondary brand color
- inherit: Uses parent element's color value

**When to use:**
- bold: Primary actions, main navigation icons, default usage
- moderate: Secondary actions, less prominent icons
- subtle: Tertiary elements, decorative icons
- *-inverse: Icons on dark backgrounds requiring light colors
- disabled/disabled-inverse: Icons in disabled state
- read-only/on-read-only-*: Icons in read-only state
- on-dark/on-light: Specific background contrast requirements
- accent/accent-subtle: Emphasized or highlighted icons
- link-*/: State-specific link icons
- negative/negative-bold: Error, destructive, or removal indicators
- warning/warning-bold: Caution or alert indicators
- positive/positive-bold: Success, completion, or confirmation indicators
- info/info-bold: Helpful information or guide indicators
- buy/sell/*: Trading-specific financial actions
- neutral/neutral-bold: Neutral semantic meaning
- brand-01/brand-02: Brand-specific icon coloring
- inherit: Match parent element text color

**Color inheritance:**
- When set to "inherit", componentColorClass() returns empty string
- Empty color string allows parent's color to apply naturally
- All other values add ion-ds-icon ion-ds-{color} classes

**Validation:**
- Invalid color values trigger console warnings
- Component validates against defined IconColor type values

## size

Controls the icon size through namespaced size values and supports responsive design strings.

**Visual cues:**
- xs: Extra small size, ideal for compact layouts or inline with small text
- sm: Small size (default), moderate compact sizing for general use
- md: Medium size, standard prominent icon display
- lg: Large size, for emphasis and primary visual elements
- inherit: Uses parent element's font-size

**When to use:**
- xs: Navigation toolbars, action buttons with space constraints, inline icons
- sm: Default choice for most applications, secondary actions, form controls
- md: Primary action indicators, dashboard icons, prominent UI elements  
- lg: Marketing content, hero sections, large emphasis points
- inherit: When icon should scale with surrounding text size

**Responsive behavior:**
- Supports MQ design strings parsed by MqDesignStringParserService
- Example format: xs=xs;sm=md;md=md;lg=lg;xl=lg;xxl=md
- Returns componentSizeClass() based on parsed size or current screen size
- Invalid size strings fall back to "md" by default

**CSS implementation:**
- Applied via componentSizeClass() computed property
- Adds classes like ion-ds-xs, ion-ds-sm, ion-ds-md, ion-ds-lg
- Special "ion-ds-size-inherit" class for inherit value sets font-size: inherit
- Sizing controlled through font shorthand with ION Icons font family

**Token resolution:**
- All sizes resolve to font: var(--ion-comp-typography-icon-*) tokens
- Tokens use font file definitions with scaling multipliers
- Actual pixel dimensions depend on the specific icon font file rendering

## ariaLabel

Provides accessibility label for screen readers and assistive technologies. Without this, decorative icons are marked as aria-hidden.

**Visual property:** None (accessibility-only)

**When to use:**
- Required when icon conveys semantic meaning or information
- Omit for purely decorative icons that don't provide content
- Use descriptive text that explains icon's purpose and function

**Accessibility behavior:**
- defaultAriaHidden() computed property returns true when ariaLabel is empty
- Empty ariaLabel results in aria-hidden="true" for decorative usage
- Non-empty ariaLabel sets aria-label attribute and removes aria-hidden
- Important for compliance with accessibility standards

**Best practices:**
- Use complete, descriptive text rather than abbreviated labels
- Describe function, not appearance (e.g., "Download PDF file" vs "Arrow down icon")
- Include relevant context when icon meaning depends on surrounding content
- Use简洁 but complete descriptions in English

## icon

**DEPRECATED:** Legacy API for icon specification. Use name and family props instead.

Controls both the icon name and font family through a single string, using space-separated format.

**Visual cues:**
- String format "family name" specifies both font family and icon name
- Single word string treated as icon name only with default family
- Parsing handled by parseIconName() and parseFamilyName() utilities

**When to use:**
- Only for backward compatibility with existing implementations
- New code should use modern name/family API instead
- Required for migration from older icon component versions

**Parsing behavior:**
- Space-separated string splits: first word becomes family, second becomes name
- Single word string: treated as name only, family defaults to empty
- Empty string: results in no icon display
- Resolves via parsedDeprecatedIcon() computed property

**Migration path:**
- Old: `icon="ION Icons check"` or `icon="check"`
- New: `name="check" family="ION Icons"` or just `name="check"`

**Warning system:**
- Console warnings displayed when deprecated icon API detected
- Tracks analytics for deprecated API usage
- Will be removed in future versions

## useDefaultPlaceholderIcon

Controls whether a placeholder icon displays when the specified icon name is invalid or not found.

**Visual property:** Affects whether placeholder icon appears (default visual) or blank space when icon validation fails

**When to use:**
- Default (undefined): Shows placeholder for invalid icon names with visual feedback
- false: Leaves icon area completely blank when icon name invalid
- true: Explicitly enables placeholder behavior (same as default/undefined)

**Validation behavior:**
- Works with updateIconName() method in icon validation logic
- Invalid icon names trigger console warnings regardless of this setting
- Controls finalIcon signal value: sets to "placeholder" or empty string
- Only applies when icon name not found in iconService.getDefaultSet()

**Use cases:**
- Leave default: Provide visual feedback for invalid icons during development
- Set to false: Clean blank display for production or when icon names must be strictly controlled
- Useful when building icon libraries or dynamic icon selection systems

**Error handling:**
- Always logs console warnings for invalid icon names
- Never suppresses validation warnings, only controls visual feedback

## compact

Forces icon size to small regardless of size prop value. Typically used in space-constrained layouts.

**Visual cues:**
- When true: Overrides size prop to render as "sm" size
- When false: Uses size prop value normally (default behavior)
- No additional visual changes beyond size adjustment

**When to use:**
- Dense data displays with limited vertical/horizontal space
- Toolbar or navigation elements requiring compact presentation
- Mobile views requiring smaller elements to fit screens
- Table cells or grid layouts with tight spacing

**Override behavior:**
- Takes precedence over both direct size prop values and MQ design strings
- Applied in updateParsedSize() method: `this.compact() ? "sm" : ...`
- Original size prop value is preserved but not rendered
- MQ design string parsing occurs after compact check

## Examples

```html
<ion-icon name="placeholder" color="bold" size="sm"></ion-icon>
```
Demonstrates default icon with bold color and small size.

```html
<ion-icon 
    name="placeholder" 
    color="inherit" 
    ariaLabel="Custom aria label. If not provided, label will be used as aria-label"
    size="inherit"></ion-icon>
```  
Demonstrates inherit color and size with custom accessibility label.

```html
<ion-icon 
    name="check" 
    family="ION Icons" 
    color="positive" 
    size="md" 
    ariaLabel="Success checkmark"></ion-icon>
```
Demonstrates custom icon name with ION Icons family, positive color state, medium size, and descriptive accessibility label.

```html
<ion-icon 
    name="delete" 
    color="negative" 
    size="xs" 
    ariaLabel="Delete item"></ion-icon>
```
Demonstrates delete icon with negative/danger color, extra small size for compact placement.

```html
<ion-icon 
    name="warning" 
    color="warning" 
    size="lg" 
    ariaLabel="Warning alert"></ion-icon>
```
Demonstrates warning icon with warning color state, large size for emphasis.

```html
<ion-icon 
    name="sell" 
    color="sell-bold" 
    size="md" 
    ariaLabel="Sell order indicator"></ion-icon>
```
Demonstrates trading-specific sell intent with bold sell color for financial application context.

## Available Icons

The icon component supports 526 unique icon names from the design system. Icons are rendered using the ION Icons font family and use snake_case naming (lowercase with underscores). When an invalid icon name is specified, a default "placeholder" icon is displayed.

A:

  - account_balance
  - account_balance_filled
  - account_circle
  - account_circle_filled
  - add
  - add_circle
  - add_circle_filled
  - add_column
  - add_column_filled
  - add_filled
  - add_order
  - add_order_filled
  - alarm
  - alarm_filled
  - area_chart
  - area_chart_filled
  - arrow_down
  - arrow_down_filled
  - arrow_left
  - arrow_left_filled
  - arrow_right
  - arrow_right_filled
  - arrow_up
  - arrow_up_filled

B:

  - backspace
  - backspace_filled
  - bar_chart
  - bar_chart_filled
  - boat
  - boat_filled
  - bottom_panel_close
  - bottom_panel_close_filled
  - bottom_panel_open
  - bottom_panel_open_filled
  - bug_report
  - bug_report_filled
  - buy
  - buy_bold
  - buy_bold_filled
  - buy_filled

C:

  - calculator
  - calculator_filled
  - calendar_add_on
  - calendar_add_on_filled
  - calendar_month
  - calendar_month_filled
  - calendar_today
  - calendar_today_filled
  - call
  - call_filled
  - cancel
  - cancel_filled
  - category
  - category_filled
  - cell_format
  - cell_format_filled
  - cell_locked
  - cell_locked_filled
  - chat
  - chat_filled
  - check
  - check_circle
  - check_circle_filled
  - check_indeterminate_small
  - check_indeterminate_small_filled
  - cheerio
  - cheerio_filled
  - chevron_collapse
  - chevron_collapse_filled
  - chevron_down
  - chevron_down_filled
  - chevron_double_left
  - chevron_double_left_filled
  - chevron_double_right
  - chevron_double_right_filled
  - chevron_expand
  - chevron_expand_filled
  - chevron_left
  - chevron_left_filled
  - chevron_right
  - chevron_right_filled
  - chevron_up
  - chevron_up_filled
  - circle
  - circle_alt
  - circle_alt_filled
  - circle_filled
  - clone
  - clone_filled
  - close
  - close_filled
  - cloud_download
  - cloud_download_filled
  - cloud_upload
  - cloud_upload_filled
  - collapse
  - collapse_area
  - collapse_area_filled
  - collapse_filled
  - columns
  - columns_filled

D:

  - dashboard
  - dashboard_alt
  - dashboard_alt_filled
  - dashboard_customize
  - dashboard_customize_filled
  - dashboard_filled
  - decrease
  - decrease_filled
  - delete
  - delete_filled
  - delete_order
  - delete_order_filled
  - density_compact
  - density_compact_filled
  - density_default
  - density_default_filled
  - density_spacious
  - density_spacious_filled
  - details
  - details_filled
  - devices
  - devices_filled
  - devices_other
  - devices_other_filled
  - donut_chart
  - donut_chart_filled
  - download
  - download_filled
  - drag_indicator
  - drag_indicator_filled

E:

  - edit
  - edit_calendar
  - edit_calendar_filled
  - edit_document
  - edit_document_filled
  - edit_filled
  - edit_off
  - edit_off_filled
  - equal
  - equal_filled
  - equalizer
  - equalizer_filled
  - error
  - error_filled
  - event_busy
  - event_busy_filled
  - expand
  - expand_area
  - expand_area_filled
  - expand_horizontal
  - expand_horizontal_filled
  - expand_vertical
  - expand_vertical_filled
  - export
  - export_filled
  - external_link
  - external_link_filled

F:

  - face_id
  - face_id_filled
  - favorite
  - favorite_filled
  - file_move
  - file_move_filled
  - filter
  - filter_alt
  - filter_alt_filled
  - filter_alt_off
  - filter_alt_off_filled
  - filter_clear
  - filter_clear_filled
  - filter_filled
  - filter_off
  - filter_off_filled
  - filter_reset
  - filter_reset_filled
  - fit_all
  - fit_all_filled
  - folder
  - folder_filled
  - folder_open
  - folder_open_filled
  - folder_shared
  - folder_shared_filled
  - folder_upload
  - folder_upload_filled
  - folder_zip
  - folder_zip_filled
  - freeze
  - freeze_filled

G:

  - grid_on
  - grid_on_filled
  - group_editor
  - group_editor_filled
  - grouping
  - grouping_filled
  - groups
  - groups_filled

H:

  - handshake
  - handshake_filled
  - help
  - help_filled
  - highlight_area
  - highlight_area_filled
  - home
  - home_filled

I:

  - idea
  - idea_filled
  - import
  - import_filled
  - info
  - info_bold
  - info_bold_filled
  - info_filled

K:

  - keyboard
  - keyboard_filled

L:

  - language
  - language_filled
  - left_panel_close
  - left_panel_close_filled
  - left_panel_open
  - left_panel_open_filled
  - link
  - link_filled
  - link_off
  - link_off_filled
  - list
  - list_filled
  - loading
  - loading_filled

M:

  - mail
  - mail_filled
  - market_depth
  - market_depth_filled
  - market_rate
  - market_rate_filled
  - menu
  - menu_filled
  - menu_horiz
  - menu_horiz_filled
  - menu_vert
  - menu_vert_filled
  - minimize
  - minimize_filled
  - move
  - move_filled
  - multiselect
  - multiselect_filled

N:

  - negative
  - negative_bold
  - negative_bold_filled
  - negative_filled
  - news
  - news_filled
  - no
  - no_filled
  - notification_add
  - notification_add_filled
  - notification_filled

O:

  - open_in_full
  - open_in_full_filled
  - open_in_new
  - open_in_new_down
  - open_in_new_down_filled
  - open_in_new_filled
  - options
  - options_filled

P:

  - password
  - password_filled
  - pause
  - pause_circle
  - pause_circle_filled
  - pdf
  - pdf_filled
  - person
  - person_filled
  - person_off
  - person_off_filled
  - pin
  - pin_filled
  - pin_number
  - pin_number_filled
  - placeholder
  - placeholder_filled
  - play_circle
  - play_circle_filled
  - popup
  - popup_filled
  - positive
  - positive_bold
  - positive_bold_filled
  - positive_filled
  - print
  - print_filled
  - public
  - public_filled
  - push
  - push_filled

R:

  - read_only
  - read_only_filled
  - redo
  - redo_filled
  - refresh
  - refresh_filled
  - remove
  - remove_circle
  - remove_circle_filled
  - remove_filled
  - rename
  - rename_filled
  - repeat
  - repeat_filled
  - replay
  - replay_filled
  - restore
  - restore_filled
  - return
  - return_filled
  - right_panel_close
  - right_panel_close_filled
  - right_panel_open
  - right_panel_open_filled

S:

  - samples
  - samples_filled
  - save
  - save_as
  - save_as_filled
  - save_filled
  - scale
  - scale_filled
  - schedule
  - schedule_filled
  - scorecard
  - scorecard_filled
  - search
  - search_add
  - search_add_filled
  - search_filled
  - sell
  - sell_bold
  - sell_bold_filled
  - sell_filled
  - send
  - send_filled
  - settings
  - settings_filled
  - share
  - share_filled
  - shared
  - shared_filled
  - side_panel
  - side_panel_filled
  - sort
  - sort2
  - sort2_filled
  - sort_down
  - sort_down_filled
  - sort_filled
  - sort_up
  - sort_up_filled
  - stop
  - stop_circle
  - stop_circle_filled
  - stop_filled
  - swap_horiz
  - swap_horiz_filled
  - swap_vert
  - swap_vert_filled
  - sync
  - sync_filled

T:

  - table
  - table_filled
  - text
  - text_filled
  - thumb_down
  - thumb_down_filled
  - thumb_up
  - thumb_up_filled
  - tiles
  - tiles_filled
  - title
  - title_filled
  - top_panel_close
  - top_panel_close_filled
  - top_panel_open
  - top_panel_open_filled
  - train
  - train_filled
  - triangle_down
  - triangle_down_filled
  - triangle_up
  - triangle_up_filled
  - truck
  - truck_filled

U:

  - undo
  - undo_filled
  - unpin
  - unpin_filled
  - unshare
  - unshare_filled
  - upload
  - upload_file
  - upload_file_filled
  - upload_filled
  - user_editor
  - user_editor_filled
  - user_error
  - user_error_filled

V:

  - vertical_align_bottom
  - vertical_align_bottom_filled
  - vertical_align_top
  - vertical_align_top_filled
  - visibility
  - visibility_filled
  - visibility_off
  - visibility_off_filled

W:

  - warning
  - warning_bold
  - warning_bold_filled
  - warning_filled
  - whatsapp
  - whatsapp_filled
  - wholesale
  - wholesale_filled
  - widgets
  - widgets_filled
  - word
  - word_filled
  - wrap_text
  - wrap_text_filled

X:

  - xls
  - xls_filled
  - xml
  - xml_filled

Y:

  - yes
  - yes_filled

Z:

  - zoom_in
  - zoom_in_filled
  - zoom_out
  - zoom_out_filled

**Notes:**
- Icons with "_filled" suffix are the filled/outline variant of the same icon
- All icon names use snake_case format (lowercase with underscores)
- The default "placeholder" icon is used when an invalid or non-existent icon name is specified
- Icons are rendered using the ION Icons font family
- Invalid icon names will trigger console warnings in development