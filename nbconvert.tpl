{%- extends 'basic.tpl' -%}

{% block header %}

<style type="text/css">
/* jupyter nbconvert */
.rendered_html code {
  background: #272822
  color: #f8f8f2;
}

div.text_cell_render {
  color: #f8f8f2 !important;
}
div.input_area {
 background: #272822 !important;
 border-color: #272822 !important;
}
div.output_area pre, div.output_stderr {
  background: var(--background-color) !important;
  color: #f8f8f2; !important;
}
div.input_prompt {
	color: #6E759D; !important;
}
.MathJax_Display,
.MathJax {
  color: #fff !important;
}
.MathJax_Display, .MathJax .mo, .MathJax .mi, .MathJax .mn {
  color: #fff !important;
}
</style>
{% endblock header %}
<!-- vim: set ft=html -->
