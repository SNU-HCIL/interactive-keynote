## Interactive Keynote

- Interactive keynote generator with python support
- Write your keynote in MD format build it
- Currently supports HCIL theme


### Environment

#### Installation

```bash
git clone https://github.com/SNU-HCIL/interactive-keynote.git

cd interactive-keynote/template
npm i
npm run dev
```

Your markdown file `myPresentation.md` should be located in `public/md`, and generated presentation can be accessed at `http://localhost:5000/myPresentation`.

#### Build

```bash
npm run build
```



### Manual

Currently follows the funtionalities provided by [grab/remark wiki](https://github.com/gnab/remark/wiki). 
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

Built-in slide classes include `left`, `center`, `right` (horizontal alignment), `top`, `middle` and `bottom` (vertical alignment), which may be used to align entire slides.

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

#### Run / Visualize Python Code

Just insert python code as usual...this will automatically generate run / visualize functionalities.

<pre>
#### Python Code

```python
def add(a,b)
  a + b
end
```</pre>

#### Multi-column Layout

Supports multi-column layout:

```markdown
.row[
.col-6[

left-column content

]
.col-6[

right-column content

]
]
```

In each row, the sum of column # should be 12. For example, you can make three columns with 2:1:1 ratio like this:

```markdown
.row[
.col-4[
first-column content
]
.col-4[
second-column content
]
.col-4[
third-column content
]
]
```

***Write code without Indentation!! Otherwise, markdown parser cannot parse your code***

#### Export PDF

A (very crude) way of printing the slides is:

1. Open in Firefox/Chrome
2. Resize the window to make the slides fill the full width of the window. (This means that there is at least a little bit of space at the top and bottom of the slides.)
3. Print to file (tip: choose a custom paper size with a 4:3 ratio)

---

Special Thanks to [sveltejs/svelte](https://github.com/sveltejs/svelte), [grab/remark](https://github.com/gnab/remark/wiki)


