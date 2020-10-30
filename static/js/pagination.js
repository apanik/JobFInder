// function initPagination() {
//
// }
//
//
// function fetchDatacallback(data){
//     var totalNumberOfData = data.count;
//     if (data.previous == null && totalNumberOfData > 0){
//         var numberOfDataInSinglePage = data.results.length;
//         var paginationSummary = "Showing 1-" + numberOfDataInSinglePage + ' of ' + totalNumberOfData + ' Jobs';
//         $('.pagination-summary').show().html(paginationSummary);
//     }
//     var list = makeListHtml(data.results, template);
//     $('.job-result').html(list);
//     var url = '/job_list';
//     var startingIndex=1;
//     makePagination(totalNumberOfData, pageSize, url, startingIndex);
//     $(".page-numbers:nth-child(2)").addClass('current');
// }
//
// function initPagination2(containerSelector, url){
//     $("body").delegate(".page-numbers", "click", function(){
//         $('.page-numbers').removeClass('current');
//         $(this).addClass('current');
//         var paginationIndex = $(this).data('value');
//         get('/api/job_list/?page='+ paginationIndex +'&page_size='+pageSize,fetchPaginationDatacallback);
//     });
// }
//
//
// function fetchPaginationDatacallback(data){
//     var currentIndex=$('.page-numbers.current').data('value');
//     var totalNumberOfData = data.count;
//     if (data.previous == null && totalNumberOfData > 0){
//         var numberOfDataInSinglePage = data.results.length;
//         var paginationSummary = "Showing 1-" + numberOfDataInSinglePage + ' of ' + totalNumberOfData + ' Jobs';
//         $('.pagination-summary').show().html(paginationSummary);
//     }
//     var list = makeListHtml(data.results, template);
//     $('.job-result').html(list);
//     var url = '/job_list';
//     makePagination(totalNumberOfData, pageSize, url, currentIndex);
//
//     $('.page-numbers[data-value=' + currentIndex + ']').addClass("current");
//
// }
// function makePagination(totalRecord, pageSize, url, startingIndex){
//     var paginationStringStart = '<nav class="navigation pagination"><div class="nav-links"><button disabled class="prev page-numbers cursor-pointer cursor-pointer" data-value="prev"><i class="fas fa-angle-left"></i></button>';
//     startingIndex = parseInt(startingIndex);
//     var numberOfPaginationIndex = totalRecord/pageSize;
//     numberOfPaginationIndex = Math.ceil(numberOfPaginationIndex);
//     var primaryNumberOfPaginationIndex = numberOfPaginationIndex;
//     var paginationIndexString = '';
//     if (numberOfPaginationIndex > 10){
//         numberOfPaginationIndex=10;
//     }
//
//     var paginationPadding = startingIndex-6
//     if (startingIndex<7){
//         startingIndex=1;
//     }else {
//         startingIndex=startingIndex-5;
//         numberOfPaginationIndex = numberOfPaginationIndex+paginationPadding;
//         if (numberOfPaginationIndex > primaryNumberOfPaginationIndex){
//             numberOfPaginationIndex = primaryNumberOfPaginationIndex;
//             //startingIndex = startingIndex-paginationPadding;
//             console.log('paginationPadding '+paginationPadding);
//             console.log('startingindex '+startingIndex);
//             var paddingStartingIndex =10-(primaryNumberOfPaginationIndex-startingIndex);
//             console.log(paddingStartingIndex);
//             startingIndex = startingIndex-paddingStartingIndex;
//         }
//     }
//
//     for (startingIndex; startingIndex <= numberOfPaginationIndex; startingIndex++){
//         if (startingIndex==1 || startingIndex==numberOfPaginationIndex){
//             var str ="<a class='page-numbers' href='javascript:void(0);' data-pazesize='"+ pageSize +"' data-value='"+ startingIndex +"' data-url='"+ url +"/?page=" + startingIndex + "&page_size="+ pageSize +"'>"+startingIndex+"</a>";
//         }else {
//             var str ="<a class='page-numbers' href='javascript:void(0);' data-pazesize='"+ pageSize +"' data-value='"+ startingIndex +"' data-url='"+ url +"/?page=" + startingIndex + "&page_size="+ pageSize +"'>"+startingIndex+"</a>";
//         }
//         paginationIndexString += str;
//
//     }
//
//     var a = '<a class="page-numbers" href="#">1</a><a class="page-numbers" href="#">3</a>' +
//         ' <a class="page-numbers" href="#">4</a>';
//
//     var paginationStringEnd = '<a class="next page-numbers" data-value="next" href="javascript:void(0);"><i class="fas fa-angle-right"></i></a></div></nav>';
//     var paginationString = paginationStringStart + paginationIndexString + paginationStringEnd;
//     $('.pagination-list').html(paginationString);
// }
