document.addEventListener("DOMContentLoaded", function(event) {
	var vip = [    
    {   
        title: "Bill Gates",   
        where: "http://www.onet.pl",   
        url: "cat1.jpg"  
    },   
    {   
        title: "Władimir Putin",   
        where: "http://www.interia.pl",   
        url: "cat2.jpg"  
    },   
    {   
        title: "Donald Trump",   
        where: "http://www.wp.pl",   
        url: "cat3.jpg"   
    }];

	// generate elements dynamically
	for(var i=0 ; i<vip.length ; ++i) {
		var item = vip[i];
		var course = $(document.createElement("div"));
		course.attr('class', 'course');
		// label
		var label = $(document.createElement("h3"));
		label.html(item.title);
		course.append(label);
		// image
		var img = $(document.createElement("img"));
		img.attr('src', item.url);
		course.append(img);
		// button
		var link = $(document.createElement("a"));
		link.attr('href', item.where);
		link.html('Gdzie jest kotek');
		course.append(link);
		$("#badges").append(course);
	}
});