$(document).ready(function(){
	$("#showMap").click(function(){
		$("#myModal").modal({
			show:true,
			backdrop:true
		});

		var map = new BMap.Map("allmap");
		var top_right_navigation = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_LEFT, type: BMAP_NAVIGATION_CONTROL_ZOOM}); //右上角，仅包含平移和缩放按钮
  		map.addControl(top_right_navigation);
		//var point = new BMap.Point(116.331398,39.897445);
		//map.centerAndZoom(point,12);
		//根据IP获取城市，并且设置城市中心点
		var myCity = new BMap.LocalCity();
		myCity.get(function moveToCity(result){
			var center = result.center;
			map.centerAndZoom(center,12);
		});

		function G(id) {
			return document.getElementById(id);
		}

		var ac = new BMap.Autocomplete({    //建立一个自动完成的对象
			"input" : "suggestId",
			"location" : map//,
			//"onSearchComplete":mySearch
		});
		ac.setInputValue("请输入装车地址并从下拉框选择准确位置");
		//function mySearch(result){
		//	alert(result.getNumPois());
		//}

		ac.addEventListener("onhighlight", function(e) {  //鼠标放在下拉列表上的事件
			var str = "";
			var _value = e.fromitem.value;
			var value = "";
			if (e.fromitem.index > -1) {
				value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
			}    
			str = "FromItem<br />index = " + e.fromitem.index + "<br />value = " + value;
			
			value = "";
			if (e.toitem.index > -1) {
				_value = e.toitem.value;
				value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
			}    
			str += "<br />ToItem<br />index = " + e.toitem.index + "<br />value = " + value;
			G("searchResultPanel").innerHTML = str;

		});

		var myValue;
		ac.addEventListener("onconfirm", function(e) {    //鼠标点击下拉列表后的事件
		var _value = e.item.value;
			myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
			G("searchResultPanel").innerHTML ="onconfirm<br />index = " + e.item.index + "<br />myValue = " + myValue;
			//输入框回显
			$("#suggestId").val(myValue);
			setPlace();
		});

		function setPlace(){
			map.clearOverlays();    //清除地图上所有覆盖物
			function myFun(){
				var pp = local.getResults().getPoi(0).point;    //获取第一个智能搜索的结果
				map.centerAndZoom(pp, 18);
				map.addOverlay(new BMap.Marker(pp));    //添加标注
			}
			var local = new BMap.LocalSearch(map, { //智能搜索
			  onSearchComplete: myFun
			});
			local.search(myValue);
		}
		});
	
})