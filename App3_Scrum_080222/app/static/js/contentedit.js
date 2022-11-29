.scrum$('button.scrum').click(function(){
    var $div=$('p.edit'), isEditable=$div.is('.editable');
    $('p.edit').prop('contenteditable',!isEditable).toggleClass('editable')
})