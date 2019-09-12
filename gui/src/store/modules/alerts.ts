/*****************************************************************************
 Filename:          alerts.ts
 Description:       Alert Store Module

 Creation Date:     30/08/2019
 Author:            Sanjeevan Bhave

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 *****************************************************************************/
import Vue from "vue";
import Vuex from "vuex";
import { Api } from "./../../services/api";
import apiRegister from "./../../services/api-register";
import { Module, VuexModule, Mutation, Action, MutationAction } from "vuex-module-decorators";
import AlertObject from "./../../models/alert";

Vue.use(Vuex);

@Module({
    namespaced: true
})
export default class Alerts extends VuexModule {
    public alerts: AlertObject | null = null;

    @Mutation
    public alertDataMutation(payload: AlertObject) {
        this.alerts = { ...payload };
    }

    @Action
    public async alertDataAction() {
        const res = await Api.getAll(apiRegister.all_alerts);
        const data = res.data;
        this.context.commit("alertDataMutation", data);
    }

    get alertTotalRecordCount() {
        if (this.alerts) {
            return this.alerts.total_records;
        }

        return;
    }

    get alertData() {
        if (this.alerts) {
            return this.alerts.alerts;
        }

        return;
    }
}
