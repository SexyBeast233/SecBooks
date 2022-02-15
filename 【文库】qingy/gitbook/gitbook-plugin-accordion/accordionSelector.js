function addAccordionSelectors(){
	var accordions = document.querySelectorAll('.accordion');
	Object.keys(accordions)
		.forEach(function(index){
			accordions[index].onclick = function(event){
				
				if(	event.target.className !== "accordionButton" &&
					event.target.className !== "accordionTitle" &&
					event.target.className !== "accordionSpinnerBox" &&
					event.target.className !== "accordionSpinner"
				) return null;

				event.stopPropagation();
				
				accordions[index].className = ~accordions[index].className.indexOf('accordionClose')
					? 'accordion'
					: 'accordion accordionClose';
			}
		})
}

require(["gitbook"], function(gitbook){
	gitbook.events.bind("page.change", addAccordionSelectors);
});