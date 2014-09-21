$(document).ready(function(){
	//datetimepicker
	$("#or_startTime").datetimepicker({
		lang:'ch'
	});

	$("#or_endTime").datetimepicker({
		lang:'ch'
	});

	$.formValidator.initConfig({formID:"publish",theme:"Default",submitOnce:true,
		onError:function(msg,obj,errorlist){
			$("#errorlist").empty();
			$.map(errorlist,function(msg){
				$("#errorlist").append("<li>" + msg + "</li>")
			});
			alert(msg);
		},
		ajaxPrompt : '有数据正在异步验证，请稍等...'
	});
	$("#or_title").formValidator({onFocus:"简要说明需求",onCorrect:"&nbsp"})
				  .regexValidator({regExp:"notempty",dataType:"enum",onError:"标题不能为空"}); 
	$("#or_start").formValidator({onFocus:"请点击图标选择",onCorrect:"&nbsp"}).functionValidator({fun:function(val,elem){
	    //点击图标就返回正确
	    return true;
		}
	});
	$("#or_end").formValidator({onCorrect:"&nbsp"})
				.regexValidator({regExp:"notempty",dataType:"enum",onError:"卸车地点不能为空"}); 

	$("#or_startTime").formValidator({onCorrect:"&nbsp"})
					  .inputValidator({min:1,onError:"can't be blank"});
	$("#or_endTime").formValidator({onCorrect:"&nbsp"})
					.inputValidator({min:1,onError:"can't be blank"});
	$("#or_name").formValidator({onCorrect:"&nbsp"})
				 .regexValidator({regExp:"notempty",dataType:"enum",onError:"can't be blank"});		
	$("#or_price").formValidator({onFocus:"RMB",onCorrect:"&nbsp"})
				  .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				  .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});	
	$("#or_board").formValidator({onFocus:"LIKE：4",onCorrect:"&nbsp"})
				  .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				  .regexValidator({regExp:"num1",dataType:"enum",onError:"Incorrect"});	
	$("#or_number").formValidator({onFocus:"",onCorrect:"&nbsp"})
				   .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:"num1",dataType:"enum",onError:"Incorrect"});
	$("#or_weight").formValidator({onFocus:"KG",onCorrect:"&nbsp"})
				   .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});
	$("#or_volume").formValidator({onFocus:"M*3",onCorrect:"&nbsp"})
	               .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});
	$("#or_length").formValidator({onFocus:"M",onCorrect:"&nbsp"})
	               .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});
	$("#or_truck").formValidator({onFocus:"Pick a type",onCorrect:"&nbsp"})
				  .inputValidator({min:1,onError: "can't be blank"}).defaultPassed();	
	$("#or_size_l").formValidator({onFocus:"M",onCorrect:"&nbsp"})
	               .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});
	$("#or_size_w").formValidator({onFocus:"M",onCorrect:"&nbsp"})
	               .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});
	$("#or_size_h").formValidator({onFocus:"M",onCorrect:"&nbsp"})
				   .inputValidator({min:1,max:10,empty:{leftEmpty:false,rightEmpty:false,emptyError:"can't be blank"},onError:"Out of range"})
				   .regexValidator({regExp:["decmal4","num1"],dataType:"enum",onError:"Incorrect"});	
	$("#or_request").formValidator({onCorrect:"&nbsp"})
				    .regexValidator({regExp:"notempty",dataType:"enum",onError:"can't be blank"});			  	 
})


function changePush(distance){
	if($("#or_start").val()==''){
		$("#or_pushTip").removeClass('onCorrect');
		$("#or_pushTip").addClass('onError');
		$("#or_pushTip").text("");
		$("#or_pushTip").append('请先选择装车地点')
		return false;
	}

	$.ajax({
        url:'/t/around/lat'+$("#or_latitude").val()+'lon'+$("#or_longitude").val()+'dis'+$("#or_push").val(),
        method:'get',
        dateType:'json',
        success:function(data){
            //alert(data.num);
            $("#or_pushTip").removeClass('onError');
            $("#or_pushTip").addClass('onCorrect');
            $("#or_pushTip").text("");
			$("#or_pushTip").append('大约有'+data.num+'辆车')
        },
        error:function(date){
        }
    });
}