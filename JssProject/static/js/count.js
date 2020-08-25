// alert("hello world") 경고창을 띄우는 로직

//text area 먼저 선택하고, 글자를 세고 싶다. 

//html 전체를 document 라고 한다. 
// const a = 변하지 않는 변수들 지정 
// let b = 값이 변하는 변수들 지정 


const targetForm = document.querySelector('.jss_content_form') //클래스를 가져온다. 
const counted_text = document.querySelector('.counted_text')
//console.log(targetForm) //console은 print 역할 
targetForm.addEventListener("keyup", function() {
    counted_text.innerHTML = targetForm.value.length
})
