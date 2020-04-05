from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from comments.models import Comment
from comments.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def comment_thread(request, id):
	#comment = get_object_or_404(Comment, id=id)
	try:
		comment = Comment.objects.get(id=id)
	except:
		raise Http404

	me = request.user.userprofile

	if not (request.user == comment.content_object.user or request.user in comment.content_object.user.userprofile.friends):
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse

	initial_data = {
		'content_type': comment.content_type,
		'object_id': comment.object_id,
	}
	comment_form = CommentForm(request.POST or None, initial=initial_data)
	if comment_form.is_valid():
		c_type = comment_form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = comment_form.cleaned_data.get("object_id")
		content_data = comment_form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
										user=request.user,
										content_type=content_type,
										object_id=obj_id,
										content=content_data,
										parent=parent_obj,
										)
		return redirect(comment.get_absolute_url())
	args = {
		'comment': comment,
		'comment_form': comment_form,
		'current_page': 'comment-thread',
		'me': me,
		}
	return render(request, "posts/comment_thread.html", args)



def comment_delete(request,comment_id, reply_id):
	#com = get_object_or_404(Comment, id=comment_id)
	try:
		com = Comment.objects.get(id=comment_id)
	except:
		raise Http404

	post_id = com.object_id
	
	if reply_id and comment_id:
		try:
			comment = Comment.objects.filter(parent__id=comment_id).get(id=reply_id)
		except:
			raise Http404
	else:
		comment = com

	if not (comment.user == request.user or request.user == comment.content_object.user):
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse
		
	comment.delete()
	messages.success(request, "comment successfully deleted!")
	if (not reply_id) and comment_id:
		return redirect("posts:view_post", pk=post_id)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))