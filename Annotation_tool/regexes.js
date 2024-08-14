var regex_names = {
 "a": "Keywords",
 "b": "Negations",
 "c": "History"
};

var colors = {

 "a": "#C1E1C1",
 "b": "#FF5733",
 "c": "#ADD8E6"
};
 


var regexes = {
  "a": [
    /subdural hematoma/gmi,
    /subdural hemorrhage/gmi,
    /sdh/gmi, 
    /acute/gmi,
    /brain injury/gmi, 
    /brain mri/gmi,
    /burr hole/gmi,
    /stable sdh/gmi,
    /craniectomy/gmi,
    /craniotomy/gmi,
    /ct head/gmi,
    /drainage/gmi,
    /evacuation/gmi,
    /head ct/gmi,
    /hematoma/gmi,
    /chronic/gmi,
    /herniation/gmi,
    /intracranial hemorrhage/gmi,
    /intraparenchymal hemorrhage/gmi,
    /midline shift/gmi,
    /mva/gmi,
    /mvc/gmi,
    /neurosurgery/gmi,
    /neurosurgical intervention/gmi,
    /scan/gmi,
    /sdh/gmi,
    /subdural/gmi,
    /tbi/gmi,
    /tentorium/gmi,
    /thickness/gmi,
    /trauma/gmi
  ],
  "b": [
    /prior/gmi,
    /recent/gmi,
    /resolved/gmi,
    /known/gmi,
    /negative/gmi,
    /no/gmi,
    /not/gmi
  ],
  "c": [
    /Principal Problem/gmi,
    /Active Problems/gmi,
    /Hospital Course/gmi,
    /Reason for Admission/gmi,
    /history/gmi,
    /hx/gmi,
    /pth/gmi,
    /pmh/gmi
  ]
};




function createDivsAndRules(regexes, colors, regex_names) {
 var row = document.getElementById('row');

 var style = document.createElement('style');
 style.appendChild(document.createTextNode(""));
 document.head.appendChild(style);

 var stylesheet = style.sheet;

 Object.entries(regexes).forEach(([key, regexArr], index) => {
   var className = "class_" + key;

   // Convert hexadecimal color to RGBA and decrease the opacity
   var color = colors[key];
   var rgbaColor = "rgba(" + parseInt(color.slice(1, 3), 16) + ", " 
     + parseInt(color.slice(3, 5), 16) + ", " 
     + parseInt(color.slice(5, 7), 16) + ", 0.5)";

   // Add a new CSS rule for this class for div elements, setting the background color with decreased opacity
   var ruleForDiv = "div." + className + " { background-color: " + rgbaColor + "; border: 1px solid "+color+" }";
   stylesheet.insertRule(ruleForDiv, stylesheet.cssRules.length);

   // Add a new CSS rule for this class for mark elements, setting the background color without changing opacity
   var ruleForMark = "mark." + className + " { background-color: " + color + "; }";
   stylesheet.insertRule(ruleForMark, stylesheet.cssRules.length);

   var newDiv = document.createElement("div");
   newDiv.className = "col " + className;
   row.appendChild(newDiv);

   // Add a rule based on the regex_names array
   var ruleForRegexName = "div." + className + "::before { content: '" + regex_names[key] + ":\n\n'; white-space: pre; }";
   stylesheet.insertRule(ruleForRegexName, stylesheet.cssRules.length);
 });
}


setTimeout(() => {createDivsAndRules(regexes, colors,regex_names)}, 500);