/* global $ */
$('textarea').summernote({ // Full toolbar without image/video functions
  height: '200',
  toolbar: [
    ['style', ['style']],
    ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript',
              'strikethrough', 'clear']],
    ['fontname', ['fontname']],
    ['fontsize', ['fontsize']],
    ['color', ['color']],
    ['para', ['ul', 'ol', 'paragraph']],
    ['height', ['height']],
    ['table', ['table']],
    ['insert', ['link', 'hr']],
    ['view', ['fullscreen', 'codeview']],
    ['help', ['help']],
  ]
});