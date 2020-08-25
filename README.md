## Interactive Keynote

- Interactive keynote generator with python support
- Write your keynote in MD format build it
- Currently supports HCIL theme

### Installation

### Manual

Currently follows the funtionalities provided by [grab/remark](https://github.com/gnab/remark/wiki). 
This document only explains basic features, which can be used without shortage while making your presentation.

#### Slide separators

A line containing *three dashes* represents a slide separator. To make an incremental slides, where succeeding slides inherits elements from previous one, use *two dashes*.

```markdown

<!-- Slide separator -->
# Slide one
blablabla
---
# Slide two
blablabla

<!-- Incremental Slide separator -->
# Silde Title 
- content 1
--
- content 2
--
- content 3

```

#### Layout

Sometimes you may want to use default *template* for repeating contents. By setting `layout: true`, you can make it. 
When set to false, reverts to using no default template.

```markdown
layout: true

#### Template subtitle

---
# Slide 1
---
# Slide 2 

<!-- both Slide 1 & 2 will contain "Template subtitle" -->

```

To designate specific slides as template, simply use `template` identifier.

```markdown
name: template-slide

Some content.

---
template: template-slide

Content appended to template-slide's content.

```


#### Title / Subtitle

Three sizes of titles are available, and subtitles can be used using ####.

```markdown
# Your Title (Big)
# Your Title (Medium)
# Your Title (Small)    
#### Your Subtitle   

```

#### Built-in Classes

Built-in slide classes include `left`, `center`, `right`, `top`, `middle` and `bottom`, which may be used to align entire slides.

```markdown
class: left, middle
# Left / Middle Aligned Title
---
class: center, middle
# Center / Middle Aligned Title
```

#### Inserting Image

Able to use markdown image inserting syntax:
```markdown
![IMAGE](./path/to/your/image.png)
```

But recommend using `<img/>` tag. Set the size of the image using the `width=n%` or `width=n px` attribute syntax 

```html
<img src="./path/to/your/image.png" width="50%" />
```

#### Inserting YouTube Video

Embed YouTube video using `<iframe/>` tag.

```markdown
class: middle, center

### Video example from YouTube
<iframe width="560" height="315" src="https://www.youtube.com/embed/5eLcHJLDlI8" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>


```



