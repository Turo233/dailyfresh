$(function(){
	    var name_error = false;
		var address_error = false;
		var stamp_error = false;
		var phone_error = false;

		// 离焦处理事件
        $(".form_group1 input").blur(function(){
            check_name();
        })

		$(".form_group2 textarea").blur(function(){
		    check_address();
		})

		$(".form_group3 input").blur(function(){
		    check_stamp();
		})

		$(".form_group4 input").blur(function(){
		    check_phone();
		})

		// 判断信息格式
		function check_name(){
            var len = $(".form_group1 input").val().length;
            if (len == 0){
				$(".form_group1 span").css('display','block');
				name_error = true;
			}
			else{
                $(".form_group1 span").css('display','none');
                name_error = false;
			}
		}

		function check_address(){
            var len = $(".form_group2 textarea").val().length;
            if (len == 0){
				$(".form_group2 span").css('display','inline-block');
				address_error = true;
			}
			else{
                $(".form_group2 span").css('display','none');
                address_error = false;
			}
		}

		function check_stamp(){
            var len = $(".form_group3 input").val().length;
            if (len != 6){
				$(".form_group3 span").css('display','block');
				stamp_error = true;
			}
			else{
                $(".form_group3 span").css('display','none');
                stamp_error = false;
			}
		}

		function check_phone(){
            var len = $(".form_group4 input").val().length;
            if (len != 11){
				$(".form_group4 span").css('display','block');
				phone_error = true;
			}
			else{
                $(".form_group4 span").css('display','none');
                phone_error = false;
			}
		}

		$(".site_check").submit(function(){
		    check_name();
			check_address();
			check_stamp();
			check_phone();

	        if (name_error == false && address_error == false &&  stamp_error == false && phone_error == false){
	            return true
			}
			else{
	            return false
			}
		})

    })