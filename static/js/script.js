// const editButtons = document.getElementsByClassName("btn-edit");
// const commentText = document.getElementById("id_body");
// const commentForm = document.getElementById("commentForm");
// const submitButton = document.getElementById("submitButton");
const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const deletePostButtons = document.getElementsByClassName("btn-delete-post");
const deletePostConfirm = document.getElementById("deletePostConfirm");
const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");



/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* Retrieves the associated comment's ID upon click.
* Updates the `deleteConfirm` link's href to point to the 
* Deletion endpoint for the specific comment.
* Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteCommentButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let postSlug = e.target.getAttribute("post_slug");
      deleteCommentConfirm.href = `/${postSlug}/delete_comment/${commentId}`;
      deleteCommentModal.show();
    });
  }


  for (let button of deletePostButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      let postSlug = e.target.getAttribute("post_slug");
      deletePostConfirm.href = `/${postSlug}/delete_post/${postId}`;
      deletePostModal.show();
    });
  }

