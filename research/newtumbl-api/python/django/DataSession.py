from django.db import models

class UserSession2(models.Model):


class AField(models.Model):
	o_min = models.CharField(max_length=255, blank=True)
	o_max = models.CharField(max_length=255, blank=True)
	s_name = models.CharField(max_length=255, blank=True)
	s_type = models.CharField(max_length=255, blank=True)
	b_numeric = models.BooleanField(blank=True, null=True)
	a_result_set = models.ForeignKey("AResultSet", blank=True)


class ARow(models.Model):
	n_width = models.FloatField(blank=True)
	sz_title = models.CharField(max_length=255, blank=True)
	b_icon_shape = models.FloatField(blank=True)
	dt_created = models.CharField(max_length=255, blank=True)
	b_t_o_s = models.FloatField(blank=True)
	b_media_type_ix = models.FloatField(blank=True)
	n_count_blog_message = models.FloatField(blank=True)
	a_result_set = models.ForeignKey("AResultSet", blank=True)
	dw_user_ix = models.FloatField(blank=True)
	n_count_post_submit = models.FloatField(blank=True)
	n_birth_year = models.FloatField(blank=True)
	qw_media_ix_icon = models.FloatField(blank=True)
	dw_admin = models.FloatField(blank=True)
	qw_media_ix = models.FloatField(blank=True)
	n_count_post_ask = models.FloatField(blank=True)
	b_logged_in = models.FloatField(blank=True)
	n_height = models.FloatField(blank=True)
	sz_body = models.CharField(max_length=255, blank=True)
	b_status = models.FloatField(blank=True)
	b_hide = models.FloatField(blank=True)
	dw_color_background = models.FloatField(blank=True)
	b_terms = models.FloatField(blank=True)
	b_rating_blogs = models.FloatField(blank=True)
	b_minor = models.FloatField(blank=True)
	dw_color_foreground = models.FloatField(blank=True)
	qw_media_ix_background = models.FloatField(blank=True)
	b_no_index = models.FloatField(blank=True)
	sz_blog_id = models.CharField(max_length=255, blank=True)
	b_active = models.FloatField(blank=True)
	b_private = models.FloatField(blank=True)
	b_verified = models.FloatField(blank=True)
	b_rating_ix = models.FloatField(blank=True)
	b_rating_blog_links = models.FloatField(blank=True)
	b_primary = models.FloatField(blank=True)
	b_block = models.FloatField(blank=True)
	dw_blog_ix = models.FloatField(blank=True)
	n_count_post_flagged = models.FloatField(blank=True)
	sz_description = models.CharField(max_length=255, blank=True)
	n_count_post_out_of_range = models.FloatField(blank=True)
	qw_media_ix_banner = models.FloatField(blank=True)
	sz_sub = models.CharField(max_length=255, blank=True)
	n_size = models.FloatField(blank=True)
	b_follow = models.FloatField(blank=True)
	dt_origin = models.CharField(max_length=255, blank=True)
	dw_i_p_address_ix = models.FloatField(blank=True)


class AResultSet(models.Model):
	user_session = models.ForeignKey("UserSession", blank=True)
	n_total_rows = models.FloatField(blank=True)


class UserSession(models.Model):
	user_session2 = models.OneToOneField("UserSession2", blank=True)
	n_result = models.CharField(max_length=255, blank=True)

