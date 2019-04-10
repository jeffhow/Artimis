/* global $ */

/**
 * Iterate through safety objectives and assign UI Classes for
 * classification based on strand identifier
 */
var topic = /^\d[.][A-Z]\s/; // 1.A (Topic)
var standard = /^\d[.][A-Z][.]\d\d\s/; // 1.A.01 (Standard)
// var objective = /^\d[.][A-Z][.]\d\d[.]\d\d/; // 1.A.01.02 (Objective)

$("[name='safety_objectives'],[name='technical_objectives'],[name='employability_objectives'],[name='management_objectives'],[name='technology_objectives']").each(function(i){
    // Remove leading whitespace
    var value = $(this).parent().text().trim();
    
    if( topic.test(value) ){
        $(this).parent().parent().addClass('topic');
    }else if( standard.test(value) ){
        $(this).parent().parent().addClass('standard');
    }else{
        $(this).parent().parent().addClass('objective');
    }
});

$('.standard').change(function(e){
    var checked = $(this).children().children('input[type="checkbox"]').prop("checked");
    $(this).nextUntil('.standard').children().children('input[type="checkbox"]').prop('checked', checked);
});

$('.topic').change(function(e){
    var checked = $(this).children().children('input[type="checkbox"]').prop("checked");
    $(this).nextUntil('.topic').children().children('input[type="checkbox"]').prop('checked', checked);
});