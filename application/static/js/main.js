    
var TabInput = []
var TabOutput = []

function removeElement(array, elem) {
  var index = array.indexOf(elem);
  if (index > -1) {
      array.splice(index, 1);
  }
}

$(document).ready( function(){

    $('input[name="input"]').amsifySuggestags({
        type :'bootstrap',
        afterAdd: function(value) {
            TabInput.push(value)
          },
          afterRemove: function(value) {
            removeElement(TabInput,value)
          }

    });

    $('input[name="output"]').amsifySuggestags({
        type :'bootstrap',
        afterAdd: function(value) {
            TabOutput.push(value)
          },
          afterRemove: function(value) {
            removeElement(TabOutput,value)
          }
    });

    $('#file').change(function(e){
      var reader = new FileReader();
      reader.readAsArrayBuffer(e.target.files[0]);
      reader.onload = function(e) {
              var data = new Uint8Array(reader.result);
              var wb = XLSX.read(data,{type:'array'});
              var htmlstr = XLSX.write(wb,{sheet:"sheet no1", type:'binary',bookType:'html'});
              $('#wrapper')[0].innerHTML += htmlstr;
      }
    });

    
})


$("#CreateModelForm").submit(function(e){
e.preventDefault()

var form = document.getElementById("CreateModelForm")
var formdata = new FormData(form)


formdata.append("input", TabInput)
formdata.append("output", TabOutput)

$.ajax({
  type: 'POST',
  url: '/CreateModal',
  data: formdata,
  contentType: false,
  cache: false,
  processData: false,
  success: function(data) {
      console.log(data);
  },
});



});



$('#file').on('change',function(){
  //get the file name
  var fileName = $(this).val();
  //replace the "Choose a file" label
  $(this).next('.custom-file-label').html(fileName);
})