$(document).ready(function(){
	$.formValidator.initConfig({formID:"client_form",theme:"Default",submitOnce:true,
		onError:function(msg,obj,errorlist){
			$("#errorlist").empty();
			$.map(errorlist,function(msg){
				$("#errorlist").append("<li>" + msg + "</li>")
			});
			alert(msg);
		},
		ajaxPrompt : '有数据正在异步验证，请稍等...'
	});

	$("#clt_mail").formValidator({onFocus:"请务必填写有效的电邮地址",onCorrect:"&nbsp"})
				  .inputValidator({min:1,onError:"电邮地址不能为空"})
				  .regexValidator({regExp:"email",dataType:"enum",onError:"email格式不正确"})
				  .ajaxValidator({
				  	type:'get',
				  	dataType:'json',
				  	//async:true,
				  	url:'/t/reg_validator/',
				  	success:function(data){
				  		if(data.msg.indexOf('yes')>=0)
				  			return true;
				  		return false;
				  	},
				  	buttons:$("#submit"),
				  	error: function(jqXHR, textStatus, errorThrown){
				  		alert("服务器忙，请重试"+errorThrown);
				  	},
					onError: "该邮箱已被注册",
					onWait: "正在校验邮箱，请稍候..."
				  }).defaultPassed();
	$("#clt_pwd").formValidator({onFocus:"6 to 15",onCorrect:"&nbsp"})
				 .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"more than 15"})
				 .regexValidator({regExp:["username"],dataType:"enum",onError:"only numbers and letters"});
	$("#clt_pwd_a").formValidator({onFocus:"6 to 15",onCorrect:"&nbsp"})
				   .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"more than 15"})
				   .compareValidator({desID:"clt_pwd",operateor:"=",onError:"doesn't match"})
				   .regexValidator({regExp:["username"],dataType:"enum",onError:"only numbers and letters"});
	$("#clt_name").formValidator({onCorrect:"&nbsp"})
				  .inputValidator({min:1,onError:"can't be blank"});
	$("#clt_tel").formValidator({onFocus:"Incorrect",onCorrect:"&nbsp"})
				 .inputValidator({min:1,onError:"can't be blank"})
				 .regexValidator({regExp:["tel","mobile"],dataType:"enum",onError:"Incorrect"});
	$("#clt_company").formValidator({onCorrect:"&nbsp"})
					 .inputValidator({min:1,onError:"can't be blank"});
	$("#confirm").inputValidator({min:1,onError:"can't be blank"});		 
})