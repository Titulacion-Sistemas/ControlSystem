/**
 * Created with PyCharm.
 * User: Jhonsson
 * Date: 12/10/14
 * Time: 12:05 AM
 * To change this template use File | Settings | File Templates.
 */


function newUrl(url) {
    window.location.assign(url)
}

function ajax(url, params)
    {
        ajaxPost(url, params, function(content){
            //onSuccess
            castear(content);
        });
    }