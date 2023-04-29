frappe.pages['gym-membership-detai'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Gym Membership Detail',
		single_column: true
	});
	$(".page-head").empty();
	$(".layout-main").empty();
	$(frappe.render_template("gym_membership_detai")).appendTo(page.wrapper);
	let gym_dashbord = new GymDashbord(wrapper);
	$(wrapper).bind('show', ()=> {
		gym_dashbord.show();
	});
}
class GymDashbord{
	constructor(wrapper) {
		this.wrapper = $(wrapper);
		this.page = wrapper.page;
		this.sidebar = this.wrapper.find('.layout-side-section');
		this.main_section = this.wrapper.find('.layout-main-section');
	}
	show() {
		frappe.breadcrumbs.add('Dashboard');
		this.sidebar.empty();
		this.setup_documents()
		let me = this;
	}
	setup_documents() {
		let me = this;
		frappe.call({
			method: 'gms.gms.page.gym_membership_detai.gym_membership_detai.get_gym_membership',
			callback: function(r) {
        if(r.message){
          let data = r.message;
				me.add_to_records(data);
				if (!data) {
					me.page.wrapper.find('.cars-list').append(`
						<div class='text-muted' align='center'>
						<br><br>${__('No more records..')}<br><br>
						</div>`);
					}
        }else{
          me.page.wrapper.find('.cars-list').append(`
						<div class='text-muted' align='center'>
						<br><br>${__('No more records..')}<br><br>
						</div>`);
        }
				}
			});
		}
		async add_to_records(data) {
			let me = this
      let remaining_days = frappe.datetime.get_day_diff(data.to_date,data.from_date)
      let details =""
			 details += `
			<div class="content page-container editable-form" style="width: 100%;">
  <div class="page-head flex">
    <div class="container">
      <div class="row flex align-center page-head-content justify-between">
        <div class="col-md-4 col-sm-6 col-xs-8 page-title">
          <div class="flex fill-width title-area">
            <div>
              <div class="flex">
                <h3 class="ellipsis title-text" title="GYM-Gym Member1--00001">${data.name}</h3>`
				if(data.status=="Active"){
					details+=`<span class="indicator-pill whitespace-nowrap green"><span>${data.status}</span></span>`
				}else if(data.status=="Deactive"){
					details+=`<span class="indicator-pill whitespace-nowrap red"><span>${data.status}</span></span>`
				}
                details+=`
              </div>
              <div class="ellipsis sub-heading hide text-muted"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container page-body">
    <div class="page-wrapper">
      <div class="page-content">
        <div class="row layout-main">
          <div class="col layout-main-section-wrapper">
            <div class="layout-main-section">
              <div>
                <div class="std-form-layout">
                  <div class="form-layout">
                    <div class="form-page">
                      <div class="row form-section card-section empty-section">
                        <div class="section-body">
                          <div class="form-column col-sm-12">
                          </div>
                        </div>
                      </div>
                      <div class="row form-section card-section visible-section">
                        <div class="section-head">
                          Details
                          <span class="ml-2 collapse-indicator mb-1" style="display: none;"></span>
                        </div>
                        <div class="section-body">
                          <div class="form-column col-sm-4">
                            <form>
                              <div class="frappe-control input-max-width">
                                <div class="form-group">
                                  <div class="clearfix">
                                    <label class="control-label reqd" style="padding-right: 0px;">Gym Member</label>
                                    <span class="help"></span>
                                  </div>
                                  <div class="control-input-wrapper">
                                    <div class="control-input" style="display: none;"></div>
                                    <div class="control-value like-disabled-input bold" style="">
                                      <a href="/app/gym-member/Gym%20Member1" >${data.gym_member}</a>
                                      </div>
                                      <p class="help-box small text-muted"></p>
                                    </div>
                                  </div>
                                </div>
                                <div class="frappe-control input-max-width">
                                  <div class="form-group">
                                    <div class="clearfix">
                                      <label class="control-label reqd" style="padding-right: 0px;">Activation date</label>
                                      <span class="help"></span>
                                    </div>
                                    <div class="control-input-wrapper">
                                      <div class="control-input" style="display: none;"></div>
                                      <div class="control-value like-disabled-input bold" style="">${data.from_date}</div>
                                      <p class="help-box small text-muted"></p>
                                    </div>
                                  </div>
                                </div>
                              </form>
                            </div>
                            <div class="form-column col-sm-4">
                              <form>
                                <div class="frappe-control input-max-width">
                                  <div class="form-group">
                                    <div class="clearfix">
                                      <label class="control-label reqd" style="padding-right: 0px;">Gym Workout Plan</label>
                                      <span class="help"></span>
                                    </div>
                                    <div class="control-input-wrapper">
                                      <div class="control-input" style="display: none;"></div>
                                      <div class="control-value like-disabled-input bold" style="">
                                        <a>${data.gym_workout_plan}</a>
                                      </div>
                                      <p class="help-box small text-muted"></p>
                                    </div>
                                  </div>
                                </div>
                                <div class="frappe-control input-max-width">
                                  <div class="form-group">
                                    <div class="clearfix">
                                      <label class="control-label" style="padding-right: 0px;">Validate Days</label>
                                      <span class="help"></span>
                                    </div>
                                    <div class="control-input-wrapper">
                                      <div class="control-input" style="display: none;"></div>
                                      <div class="control-value like-disabled-input" style="">${remaining_days}</div>
                                      <p class="help-box small text-muted"></p>
                                    </div>
                                  </div>
                                </div>
                                <div class="frappe-control input-max-width">
                                  <div class="form-group">
                                    <div class="clearfix">
                                      <label class="control-label" style="padding-right: 0px;">To Date</label>
                                      <span class="help"></span>
                                    </div>
                                    <div class="control-input-wrapper">
                                      <div class="control-input" style="display: none;"></div>
                                      <div class="control-value like-disabled-input" style="">${data.to_date}</div>
                                      <p class="help-box small text-muted"></p>
                                    </div>
                                  </div>
                                </div>
                                <div class="frappe-control input-max-width">
                                  <div class="form-group">
                                    <div class="clearfix">
                                      <label class="control-label" style="padding-right: 0px;">Total Amount</label>
                                      <span class="help"></span>
                                    </div>
                                    <div class="control-input-wrapper">
                                      <div class="control-input" style="display: none;"></div>
                                      <div class="control-value like-disabled-input" style="">₹ ${data.total_amount}</div>
                                      <p class="help-box small text-muted"></p>
                                    </div>
                                  </div>
                                </div></form>
                              </div><div class="form-column col-sm-4">
                                <form>
                                  <div class="frappe-control input-max-width">
                                    <div class="form-group">
                                      <div class="clearfix">
                                        <label class="control-label reqd" style="padding-right: 0px;">Durnation</label>
                                        <span class="help"></span>
                                      </div>
                                      <div class="control-input-wrapper">
                                        <div class="control-input" style="display: none;"></div>
                                        <div class="control-value like-disabled-input bold" style="">${data.durnation}</div>
                                        <p class="help-box small text-muted"></p>
                                      </div>
                                    </div>
                                  </div>
                                </form>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>`
			this.page.wrapper.find('.cars-list').append(details);
		}
}