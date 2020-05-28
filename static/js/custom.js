$(function(){
	$('.search_btn').on('click',function(){
		$(".search_open, .search_close").toggleClass("search_open search_close");
			$('.search').toggleClass('search_active');
			$('.go_btn').toggleClass('search_active_go_btn');
		});
});