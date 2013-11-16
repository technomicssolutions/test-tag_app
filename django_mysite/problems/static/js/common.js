var ExpandableMenu = new Class({
    Implements: [Options, Events],
    options: {

    },
    initialize: function(element, options) {
        this.topic_flag = false;
        this.concept_flag = false;
        this.element = element;
        this.setOptions(options);
        this.subject_lis = this.element.getElements('.subjects_li');
        this.subject_lis.each(function(li, index){
            li.addEvent('click', function(ev){
                ev.stop();
                if(li.hasClass('shrink')) {
                    li.set('html', '-');
                    li.addClass('expand').removeClass('shrink');
                    li.getParent().getElement('ul').setStyle('display', 'block');
                } else {
                    li.set('html', '+');
                    li.addClass('shrink').removeClass('expand');
                    li.getParent().getElement('ul').setStyle('display', 'none');
                }
            }.bind(this));
        }.bind(this));

    },
})


window.addEvent('domready', function(){
    
    if($$('.subject').length) {
        var el = new ExpandableMenu($$('.subject')[0], {});
    }
        
    $$('.add_topic').hide();
    $$('.add_concept').hide();
    $$('.add_new_concept').hide();
    $$('.add_new_topic').addEvent('click', function(e){
        e.stop();
        $$('.add_topic').show();
        $$('.add_new_concept').show();
    }); 
    $$('.add_new_concept').addEvent('click', function(e){
        e.stop();
        $$('.add_concept').show();
    }); 
    $$('.save_subject').addEvent('click', function(e){

        var subject = $$('.subject_form').toQueryString();
        var url = 'add_subject/';
        var ajaxRequest = new Request({
            url: url,
            method: 'post',
            data: subject,
            onSuccess: function(){
                console.log('Success');
            },
            onFailure: function(){
                console.log('failure');
                console.log(this.getHeader('Status'));
            },
            onException: function(headerName, value) {
                console.log('exception');
                console.log(headerName+': '+value);
            }
        });
        ajaxRequest.send(); 
    });
    
});