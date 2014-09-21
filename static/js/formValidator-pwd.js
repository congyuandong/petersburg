$(document).ready(function(){
	$.formValidator.initConfig({formID:"pwd",theme:"Default",submitOnce:true,
		onError:function(msg,obj,errorlist){
			$("#errorlist").empty();
			$.map(errorlist,function(msg){
				$("#errorlist").append("<li>" + msg + "</li>")
			});
			alert(msg);
		},
		ajaxPrompt : '有数据正在异步验证，请稍等...'
	});
	$("#o_pwd").formValidator({onCorrect:"&nbsp"})
			   .inputValidator({min:1,onError:"can't be blank"});
	$("#new_pwd").formValidator({onFocus:"6 to 15",onCorrect:"&nbsp"})
				 .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"more than 15"})
				 .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"only numbers and letters"});
	$("#new_pwd_a").formValidator({onFocus:"6 to 15",onCorrect:"&nbsp"})
				   .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"ore than 15"})
				   .compareValidator({desID:"new_pwd",operateor:"=",onError:"doesn't match"})
				   .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"only numbers and letters"});
})