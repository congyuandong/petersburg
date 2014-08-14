// JavaScript Document
$(document).ready(function(){
	var selects=$('select');//获取select
for(var i=0;i<selects.length;i++){
  createSelect(selects[i],i);
}
function createSelect(select_container,index){
  //创建select容器，class为select_box，插入到select标签前
  var tag_select=$('<div></div>');//div相当于select标签
  tag_select.attr('class','select_box');
  tag_select.insertBefore(select_container);
  //显示框class为select_showbox,插入到创建的tag_select中
  var select_showbox=$('<div></div>');//显示框
  select_showbox.css('cursor','pointer').attr('class','select_showbox').appendTo(tag_select);
  //创建option容器，class为select_option，插入到创建的tag_select中
  var ul_option=$('<ul></ul>');//创建option列表
  ul_option.attr('class','select_option');
  ul_option.appendTo(tag_select);
  createOptions(index,ul_option);//创建option
  //点击显示框
  tag_select.toggle(function(){
    ul_option.show();
  },function(){
    ul_option.hide();
  });
  var li_option=ul_option.find('li');
  li_option.on('click',function(){
    $(this).addClass('selected').siblings().removeClass('selected');
    var value=$(this).text();
    select_showbox.text(value);
    ul_option.hide();
  });
  li_option.hover(function(){
    $(this).addClass('hover').siblings().removeClass('hover');
  },function(){
    li_option.removeClass('hover');
  });
}
function createOptions(index,ul_list){
  //获取被选中的元素并将其值赋值到显示框中
  var options=selects.eq(index).find('option'),
    selected_option=options.filter(':selected'),
    selected_index=selected_option.index(),
    showbox=ul_list.prev();
    showbox.text(selected_option.text());
  //为每个option建立个li并赋值
  for(var n=0;n<options.length;n++){
    var tag_option=$('<li></li>'),//li相当于option
      txt_option=options.eq(n).text();
    tag_option.text(txt_option).css('cursor','pointer').appendTo(ul_list);
    //为被选中的元素添加class为selected
    if(n==selected_index){
      tag_option.attr('class','selected');
    }
  }
}

	
	
	function resetloc(){
		//$(".banner > .wrap > .item:eq(1)").css("left","0px");
		$(".banner > .wrap > .item:eq("+ $(".banner .switch .hover").attr("data") +")").css("left","0px").show();
		$(".banner .temp").css("left","1000px");
	}
	function tooglebanner(o){
		var obj;
		if(o == null){
			//alert(($(".banner .switch .hover").attr("data") * 1 + 1) < ($(".banner .wrap .switch li").size()*1));
			var n = ($(".banner .switch .hover").attr("data") * 1) < ($(".banner .wrap .switch li").size()*1-1)?$(".banner .switch .hover").attr("data"):-1;
			obj = $(".banner .switch li:eq("+(n*1+1)+")");
		}
		else{obj = o;}
		$(".banner .switch li").removeClass("hover");
		obj.addClass("hover");
		obj.parent(".switch").parent(".wrap").children(".item").animate({left:"-1000px"},3000);
		$(".banner .temp").html(obj.parent(".switch").parent(".wrap").children(".item:eq("+obj.attr("data")+")").html()).animate({left:"0px"},3000,resetloc);
	}
	$(".banner .switch li").click(function(){
		tooglebanner($(this));
	});
	
	var changebanner = setInterval(tooglebanner,5000);
	$(".banner .wrap").mouseover(function(){
		clearInterval(changebanner);
	});
	$(".banner .wrap").mouseout(function(){
		changebanner = setInterval(tooglebanner,5000);
	});
	
	
	$(".extend").click(function(){
		if($(this).attr("class") == "extend"){
			$(this).addClass("pack");
			$(this).children("a").html("收起");
			$(this).parent("div").children("span").show();
		}
		else{
			$(this).removeClass("pack");
			$(this).children("a").html("更多");
			$(this).parent("div").children(".ep").hide();
		}
	});
	
})
// JavaScript Document



function showBg() { 
  var bh = $("body").height(); 
  var bw = $("body").width(); 
  $(".fullbg").css({ 
  height:bh, 
  width:bw, 
  display:"block" 
  }); 
  $(".dialog").show(); 
} 
  //关闭灰色 jQuery 遮罩 
function closeBg() { 
  $(".fullbg, .dialog").hide(); 
}